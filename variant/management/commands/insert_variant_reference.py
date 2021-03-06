"""Insert variant analysis results into database."""
import sys
from cyvcf2 import VCF
import time

from django.db import connection, transaction
from django.db.utils import IntegrityError
from django.core.management.base import BaseCommand, CommandError

from staphopia.utils import timeit
from variant.models import Annotation, Feature, Comment, Reference, SNP


class Command(BaseCommand):
    """Insert results into database."""

    help = 'Insert the analysis results into the database.'

    def add_arguments(self, parser):
        """Command line arguements."""
        parser.add_argument('input', metavar='INPUT_VCF',
                            help=('Annotated VCF formated file to '
                                  'be inserted'))
        parser.add_argument('--compressed', action='store_true',
                            help='Input VCF is gzipped.')
        parser.add_argument('--empty', action='store_true',
                            help='Empty tables and reset counts.')

    def handle(self, *args, **opts):
        """Insert results to database."""
        if opts['empty']:
            # Empty Tables
            self.empty_tables()
            sys.exit()

        # Open VCF for reading
        self.open_vcf(opts['input'])

        # Get reference info
        self.get_reference_instance()

        # Get data already in the DB
        self.get_annotation_instances()
        self.get_feature_instances()
        self.get_locus_tags()
        self.get_comments()
        self.get_comment_instances()

        # Store variants for bulk create
        self.snps = []

        # Read through VCF
        self.time = time.time()
        self.read_vcf()

        # Ready to insert variants
        self.insert_snps()

    @timeit
    def open_vcf(self, vcf_file):
        """Read input VCF file."""
        try:
            self.vcf_reader = VCF(vcf_file)
        except IOError:
            raise CommandError('{0} does not exist'.format(input))

    @transaction.atomic
    def get_reference_instance(self):
        """Get reference instance."""
        try:
            r = self.vcf_reader.seqnames[0]
            self.reference, created = Reference.objects.get_or_create(
                name=r
            )
        except IntegrityError:
            raise CommandError('Error getting/saving reference information')

    def get_locus_tags(self):
        """Return the primary key of each locus tag."""
        self.locus_tags = {}
        for tag in Annotation.objects.filter(reference=self.reference):
            self.locus_tags[tag.locus_tag] = tag.pk

    def get_annotation_instances(self):
        """Return the instance for each annotation."""
        pks = []
        for ks in Annotation.objects.filter(reference=self.reference):
            pks.append(ks.pk)
        self.annotations = Annotation.objects.in_bulk(pks)

    def get_comments(self):
        """Return the primary key of each comment."""
        self.comments = {}
        for c in Comment.objects.all():
            self.comments[c.comment] = c.pk

    def get_comment_instances(self):
        """Return the instance for each comment."""
        pks = []
        for ks in Comment.objects.all():
            pks.append(ks.pk)
        self.comment_instances = Comment.objects.in_bulk(pks)

    @transaction.atomic
    def get_annotation(self, record):
        """Get or create annotations."""
        annotation = None
        locus_tag = record.INFO['LocusTag']
        if locus_tag in self.locus_tags:
            pk = self.locus_tags[locus_tag]
            annotation = self.annotations[pk]
        elif locus_tag == '.':
            if 'inter_genic' not in self.locus_tags:
                annotation = Annotation.objects.create(
                    reference=self.reference,
                    locus_tag='inter_genic',
                    protein_id='inter_genic',
                    gene='inter_genic',
                    product='inter_genic',
                    note='inter_genic',
                    is_pseudo=record.INFO['IsPseudo']
                )
                self.locus_tags['inter_genic'] = annotation.pk
                self.annotations[annotation.pk] = annotation
            else:
                pk = self.locus_tags['inter_genic']
                annotation = self.annotations[pk]
        else:
            protein_id = record.INFO['ProteinID']
            if protein_id == '.':
                protein_id = "not_applicable"

            annotation = Annotation.objects.create(
                reference=self.reference,
                locus_tag=locus_tag,
                protein_id=protein_id,
                gene=('.' if record.INFO['Gene'] is None
                      else record.INFO['Gene']),
                product=('.' if record.INFO['Product'] is None
                         else record.INFO['Product']),
                note=('.' if record.INFO['Note'] is None
                      else record.INFO['Note']),
                is_pseudo=record.INFO['IsPseudo']
            )
            self.locus_tags[locus_tag] = annotation.pk
            self.annotations[annotation.pk] = annotation

        return annotation

    @transaction.atomic
    def get_comment(self, c):
        """Get or create comment instances."""
        comment = None
        if c is None:
            c = 'None'

        if c in self.comments:
            pk = self.comments[c]
            comment = self.comment_instances[pk]
        else:
            comment = Comment.objects.create(comment=c)
            self.comments[c] = comment.pk
            self.comment_instances[comment.pk] = comment

        return comment

    def get_feature_instances(self):
        """Return the primary key of each feature type."""
        self.features = {}
        for tag in Feature.objects.filter(reference=self.reference):
            self.features[tag.feature] = tag

    def get_feature(self, feature):
        """Get the feature type of a variant."""
        if feature in self.features:
            return self.features[feature]
        else:
            try:
                feature_obj = Feature.objects.create(
                    reference=self.reference,
                    feature=feature
                )
                self.features[feature] = feature_obj
                return feature_obj
            except IntegrityError:
                raise CommandError('Error getting/saving feature information')

    @transaction.atomic
    def create_snp(self, record, reference, annotation, feature):
        """Add new SNP to list to bulk insert later."""
        self.snps.append(SNP(
            reference=reference,
            annotation=annotation,
            feature=feature,
            reference_position=record.POS,
            reference_base=record.REF,
            alternate_base=record.ALT[0],

            reference_codon=(
                '.' if record.INFO['RefCodon'][0] is None
                else record.INFO['RefCodon']
            ),
            alternate_codon=(
                '.' if record.INFO['AltCodon'][0] is None
                else record.INFO['AltCodon']
            ),
            reference_amino_acid=(
                record.INFO['RefAminoAcid'] if record.INFO['RefAminoAcid']
                else '.'
            ),
            alternate_amino_acid=(
                record.INFO['AltAminoAcid'] if record.INFO['AltAminoAcid']
                else '.'
            ),
            codon_position=(
                0 if record.INFO['CodonPosition'] is None
                else record.INFO['CodonPosition']
            ),
            snp_codon_position=(
                0 if record.INFO['SNPCodonPosition'] is None
                else record.INFO['SNPCodonPosition']
            ),
            amino_acid_change=(
                '.' if record.INFO['AminoAcidChange'][0] is None
                else record.INFO['AminoAcidChange']
            ),
            is_synonymous=record.INFO['IsSynonymous'],
            is_transition=record.INFO['IsTransition'],
            is_genic=record.INFO['IsGenic'],
        ))

    def read_vcf(self):
        """Read throught VCF Records."""
        count = 0

        for record in self.vcf_reader:
            # Get annotation, filter, comment
            annotation = self.get_annotation(record)
            feature = self.get_feature(record.INFO['FeatureType'])

            # Insert SNP/Indel
            if record.is_snp:
                self.get_comment(record.INFO['Comments'])
                self.create_snp(record, self.reference, annotation, feature)
                count += 1
                if count % 100000 == 0:
                    total_time = f'{time.time() - self.time:.2f}'
                    rate = f'{100000 / float(total_time):.2f}'
                    print(''.join([
                        f'Processed 100k, Total {count} SNPs ',
                        f'(took {total_time}s, {rate} snp/s)'
                    ]))
                    self.time = time.time()

    @transaction.atomic
    def insert_snps(self):
        """Insert SNPs in bulk."""
        SNP.objects.bulk_create(self.snps, batch_size=2000)
        return None

    @transaction.atomic
    def empty_tables(self):
        """Empty Tables and Reset id counters to 1."""
        tables = ['variant_snp', 'variant_indel', 'variant_annotation',
                  'variant_comment', 'variant_feature', 'variant_filter']

        for table in tables:
            self.empty_table(table)

    def empty_table(self, table):
        """Empty Table and Reset id counters to 1."""
        print("Emptying {0}...".format(table))
        query = "TRUNCATE TABLE {0} RESTART IDENTITY CASCADE;".format(table)
        cursor = connection.cursor()
        cursor.execute(query)
