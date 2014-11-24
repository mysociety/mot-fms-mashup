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

            # ['334881', 'GU', '51.172109650377', '-0.46403161059507']
            reader.next() # discard header row

            count = 0

            for (fms_report_id, code, latitude, longitude) in reader:
                (postcode, _) = Postcode.objects.get_or_create( code=code );
                FMSReport.objects.create(
                    fms_report_id=fms_report_id,
                    latitude=latitude,
                    longitude=longitude,
                    postcode=postcode
                )
                count += 1

            print "Imported %d records" % count
                    


