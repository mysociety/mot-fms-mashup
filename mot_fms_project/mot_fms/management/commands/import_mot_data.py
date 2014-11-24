from django.core.management.base import BaseCommand, CommandError
from mot_fms.models import Postcode, Vehicle, VehicleMake
from datetime import datetime
import csv

class Command(BaseCommand):
    help = 'Imports '

    def add_arguments(self, parser):
        # parser.add_argument('poll_id', nargs='+', type=int)
        pass

    def handle(self, *args, **options):
        with open('data/makes.txt', 'r') as f:
            reader = csv.reader(f, delimiter='|')
            for (make_id, make) in reader:
                VehicleMake.objects.get_or_create(pk=make_id, make=make)

        with open('data/vehicles_with_models.txt', 'r') as f:
            reader = csv.reader(f, delimiter='|')
            for (vehicle_id, make_id, model, first_use_date, fuel_type, passed_first_time, mileage, mot_date, postcode_str) in reader:
                (postcode, _) = Postcode.objects.get_or_create(pk=postcode_str)
                default_values = {
                    'make_id': make_id,
                    'model_info': model,
                    'first_use_date': datetime.strptime(first_use_date, '%Y-%m-%d'),
                    'fuel_type': fuel_type,
                    'passed_first_time': passed_first_time,
                    'mileage': mileage,
                    'mot_date': datetime.strptime(mot_date, '%Y-%m-%d'),
                    'postcode': postcode,
                }
                Vehicle.objects.get_or_create(pk=vehicle_id, defaults=default_values)
