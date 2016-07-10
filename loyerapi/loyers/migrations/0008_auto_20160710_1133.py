# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-10 11:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loyers', '0007_auto_20160710_0757'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loyer',
            old_name='agglomeration_link',
            new_name='agglomeration',
        ),
        migrations.RenameField(
            model_name='loyer',
            old_name='agglomeration_description_link',
            new_name='agglomeration_description',
        ),
        migrations.RenameField(
            model_name='loyer',
            old_name='construction_period_link',
            new_name='construction_period',
        ),
        migrations.RenameField(
            model_name='loyer',
            old_name='housing_type_link',
            new_name='housing_type',
        ),
        migrations.RenameField(
            model_name='loyer',
            old_name='number_of_rooms_link',
            new_name='number_of_rooms',
        ),
        migrations.RenameField(
            model_name='loyer',
            old_name='observatory_link',
            new_name='observatory',
        ),
        migrations.RenameField(
            model_name='loyer',
            old_name='production_methodology_link',
            new_name='production_methodology',
        ),
        migrations.RenameField(
            model_name='loyer',
            old_name='renter_seniority_link',
            new_name='renter_seniority',
        ),
        migrations.RenameField(
            model_name='loyer',
            old_name='Data_year',
            new_name='year',
        ),
        migrations.RemoveField(
            model_name='loyer',
            name='surface_moyenne',
        ),
        migrations.AlterField(
            model_name='loyer',
            name='loyer_moyen',
            field=models.IntegerField(max_length=200, null=True),
        ),
    ]