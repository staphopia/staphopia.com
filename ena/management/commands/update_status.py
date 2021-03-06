'''
    Robert Petit

    Outputs Experiments and corresponding runs information in JSON format.
'''
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError

from ena.models import Experiment, Status


class Command(BaseCommand):

    """ . """

    help = 'Insert ENA data information into the database.'

    def add_arguments(self, parser):
        """Command line arguements."""
        parser.add_argument('experiment', help='Experiment to update.')
        parser.add_argument('status', help='Current status of the job.')
        parser.add_argument('--server', help='Server job is processed on.')
        parser.add_argument('--path', help='Location of the job.')
        parser.add_argument('--delete', action='store_true',
                            help='Delete experiment from table.')
        parser.add_argument('--get', action='store_true',
                            help='Get status of experiment.')

    def handle(self, *args, **options):
        # ENA to Sample
        if options['delete']:
            Status.objects.filter(
                experiment_accession=options['experiment']
            ).delete()
        elif options['get']:
            try:
                to_sample = Status.objects.get(
                    experiment_accession=options['experiment']
                )
                print('{0}\t{1}\t{2}\t{3}'.format(
                    to_sample.experiment_accession,
                    to_sample.server,
                    to_sample.path,
                    to_sample.status
                ))
            except Status.DoesNotExist:
                print('{0} does not exist.'.format(options['experiment']))
        else:
            try:
                experiment = Experiment.objects.get(
                    experiment_accession=options['experiment']
                )
                if options['server'] and options['path']:
                    try:
                        ena_to_sample, c = Status.objects.update_or_create(
                            experiment_accession=experiment,
                            server=options['server'],
                            status=options['status'],
                            path=options['path'],
                        )
                    except IntegrityError:
                        Status.objects.filter(
                            experiment_accession=experiment
                        ).update(
                            server=options['server'],
                            status=options['status'],
                            path=options['path'],
                        )
                else:
                    try:
                        ena_to_sample, c = Status.objects.update_or_create(
                            experiment_accession=experiment,
                            status=options['status'],
                        )
                    except IntegrityError:
                        Status.objects.filter(
                            experiment_accession=experiment
                        ).update(
                            status=options['status'],
                        )
            except Experiment.DoesNotExist:
                print('{0} does not exist.'.format(options['experiment']))
