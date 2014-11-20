from django.db import models

class Postcode(models.Model):
    code = models.CharField(max_length=4) # just the 'E' part
