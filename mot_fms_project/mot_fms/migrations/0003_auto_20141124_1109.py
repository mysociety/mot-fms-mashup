# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mot_fms', '0002_auto_20141120_1615'),
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleMake',
            fields=[
                ('make_id', models.IntegerField(serialize=False, primary_key=True)),
                ('make', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RunSQL(
          sql=
              'ALTER TABLE "mot_fms_vehicle" '
              'ALTER COLUMN "make" SET DATA TYPE integer '
              'USING (make::integer);',
          reverse_sql =
              'ALTER TABLE "mot_fms_vehicle" '
              'ALTER COLUMN "make" SET DATA TYPE varchar(30);',
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='make',
            field=models.ForeignKey(to='mot_fms.VehicleMake'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='vehicle',
            name='model_info',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
    ]
