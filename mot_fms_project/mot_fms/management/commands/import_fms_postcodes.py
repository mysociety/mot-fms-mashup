from django.core.management.base import BaseCommand, CommandError
from mot_fms.models import Postcode, FMSReport
import csv

class Command(BaseCommand):
    help = 'Imports '

    def add_arguments(self, parser):
        # parser.add_argument('poll_id', nargs='+', type=int)
        pass

    def handle(self, *args, **options):
        with open('data/fms-postcodes.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                print row
