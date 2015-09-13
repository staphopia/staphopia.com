""" Insert JSON formatted assembly results into database. """
import json
import os.path

from django.db import transaction
from django.db.utils import IntegrityError
from django.core.management.base import BaseCommand, CommandError

from sample.models import MetaData
from assembly.models import Stats


class Command(BaseCommand):
    """ Insert results into database. """
    help = 'Insert the assembly results into the database.'

    
    def add_arguments(self, parser):
        parser.add_argument('sample_tag', metavar='SAMPLE_TAG',
                            help='Sample tag of the data.')
        parser.add_argument('table', metavar='TABLE',
                            help='Table (contigs or scaffolds) to insert into.')
        parser.add_argument('input', metavar='JSON_INPUT',
                            help='JSON formated file to be inserted')

    @transaction.atomic
    def handle(self, *args, **opts):
        """ Insert results to database. """

        # Sample (sample.MetaData)
        try:
            sample = MetaData.objects.get(sample_tag=opts['sample_tag'])
        except MetaData.DoesNotExist:
            raise CommandError('sample_tag: {0} does not exist'.format(
                opts['sample_tag']
            ))

        # Database Table
        accepted_tables = ['contigs', 'scaffolds']
        if opts['table'] not in accepted_tables:
            raise CommandError(
                'Unknown table: {0}. Use one of the following: {1}'.format(
                    opts['table'],
                    ', '.join(accepted_tables)
                )
            )

        # Input File
        if not os.path.exists(opts['input']):
            raise CommandError('{0} does not exist'.format(opts['input']))

        # JSON input
        try:
            with open(opts['input'], 'r') as f:
                json_data = json.loads(f.readline().rstrip())
        except ValueError as e:
            raise CommandError('{0}: invalid JSON'.format(opts['input']))

        # Everything checks out, load it up
        try:
            is_scaffolds = False if opts['table'] == 'contigs' else True
            table_object = Stats(
                sample=sample,
                is_scaffolds=is_scaffolds,
                **json_data
            )
            table_object.save()
            print 'Saved results'
        except IntegrityError as e:
            raise CommandError(
                ('{0}. Either the data is already in there or the pipeline '
                 'version should be updated.').format(e)
            )
