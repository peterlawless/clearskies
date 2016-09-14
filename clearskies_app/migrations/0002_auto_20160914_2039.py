# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-14 20:39
from __future__ import unicode_literals

from django.db import migrations
import csv


def load_data(apps, schema_editor):
    Airfield = apps.get_model('clearskies_app', 'Airfield')

    with open('airports_NorthAm_only_K.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            temp = Airfield(identifier=row[1], name=row[3],
                            latitude=float(row[4]), longitude=float(row[5]),
                            state=row[9][-2:], city=row[10])
            temp.save()


class Migration(migrations.Migration):

    dependencies = [
        ('clearskies_app', '0001_initial'),
    ]
 
    operations = [
        migrations.RunPython(load_data)
    ]
