"""
Sequence Application Models.

These are models to store information on the sequence quality of Staphopia
samples.
"""
from django.db import models

from sample.models import Sample
from version.models import Version


class Stage(models.Model):
    """Store the cleanup stage of the FASTQ stats"""
    name = models.TextField(unique=True)


class Summary(models.Model):
    """Summary statistics of input FASTQ file."""
    sample = models.ForeignKey(Sample, on_delete=models.CASCADE,
                               related_name='sequence_summary_sample')
    version = models.ForeignKey(Version, on_delete=models.CASCADE,
                                related_name='sequence_summary_version')
    is_paired = models.BooleanField(default=False, db_index=True)
    stage = models.ForeignKey('Stage', on_delete=models.CASCADE)
    rank = models.PositiveSmallIntegerField(db_index=True)

    total_bp = models.BigIntegerField()
    coverage = models.DecimalField(max_digits=7, decimal_places=2)

    read_total = models.BigIntegerField(default=0)
    read_min = models.PositiveIntegerField(default=0)
    read_mean = models.DecimalField(default=0.0, max_digits=11,
                                    decimal_places=4)
    read_std = models.DecimalField(default=0.0, max_digits=11,
                                   decimal_places=4)
    read_median = models.PositiveIntegerField(default=0)
    read_max = models.PositiveIntegerField(default=0)
    read_25th = models.PositiveIntegerField(default=0)
    read_75th = models.PositiveIntegerField(default=0)
    read_lengths = models.TextField()

    qual_mean = models.DecimalField(max_digits=7, decimal_places=4)
    qual_std = models.DecimalField(max_digits=7, decimal_places=4)
    qual_median = models.PositiveIntegerField()
    qual_25th = models.PositiveIntegerField()
    qual_75th = models.PositiveIntegerField()
    qual_per_base = models.TextField()

    class Meta:
        unique_together = ('sample', 'version', 'stage')

    def sample_tag(self):
        """Display sample tag in admin view."""
        return self.sample.sample_tag
    sample_tag.short_description = 'Sample Tag'
    sample_tag.admin_order_field = 'sample'

    def sequence_rank(self):
        """Display medal rank in admin view."""
        ranks = {1: 'Bronze', 2: 'Silver', 3: 'Gold'}
        return ranks[self.rank]
    sequence_rank.short_description = 'Rank'
    sequence_rank.admin_order_field = 'rank'
