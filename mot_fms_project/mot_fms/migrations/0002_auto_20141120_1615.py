# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mot_fms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postcode',
            name='id',
        ),
        migrations.AlterField(
            model_name='postcode',
            name='code',
            field=models.CharField(max_length=4, serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='FMSReport',
            fields=[
                ('fms_report_id', models.IntegerField(serialize=False, primary_key=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('postcode', models.ForeignKey(related_name='reports', to='mot_fms.Postcode')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('vehicle_id', models.IntegerField(serialize=False, primary_key=True)),
                ('make', models.CharField(max_length=30)),
                ('first_use_date', models.DateField()),
                ('fuel_type', models.CharField(max_length=1)),
                ('passed_first_time', models.BooleanField()),
                ('mileage', models.IntegerField()),
                ('mot_date', models.DateField()),
                ('postcode', models.ForeignKey(to='mot_fms.Postcode')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
