from django.db import models

class Postcode(models.Model):
    code = models.CharField(max_length=4, primary_key=True) # just the 'E' part

class VehicleMake(models.Model):
    make_id = models.IntegerField(primary_key=True)
    make = models.CharField(max_length=30)

class Vehicle(models.Model):
    vehicle_id = models.IntegerField(primary_key=True)
    make = models.ForeignKey(VehicleMake)
    model_info = models.CharField(max_length=100)
    first_use_date = models.DateField()
    fuel_type = models.CharField(max_length=1)
    passed_first_time = models.BooleanField()
    mileage = models.IntegerField()
    mot_date = models.DateField()
    postcode = models.ForeignKey(Postcode)

class FMSReport(models.Model):
    fms_report_id = models.IntegerField(primary_key=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    postcode = models.ForeignKey(Postcode, related_name='reports')

