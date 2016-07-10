# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-09 08:37
from __future__ import unicode_literals
import csv

from django.db import migrations


def import_csv(apps, schema_editor):
    Loyer = apps.get_model("loyers", "Loyer")
    with open('../Base_OP_2014_Nationale.csv', 'rb') as csvfile:
        loyerreader = csv.reader(csvfile, delimiter=str(u';'), quotechar=str(u'|'))
        next(loyerreader, None)
        for row in loyerreader:
            print row
            loyer = Loyer(Observatory=row[0], Data_year=row[1], agglomeration=row[2], Zone_complementaire=row[3], Type_habitat=row[4], epoque_construction_homogene=row[5], anciennete_locataire_homogene=row[6], nombre_pieces_homogene=row[7], loyer_1_decile=row[8], loyer_1_quartile=row[9], loyer_median=row[10], loyer_3_quartile=row[11], loyer_9_decile=row[12], loyer_moyen=row[13], loyer_mensuel_1_decile=row[14], loyer_mensuel_1_quartile=row[15], loyer_mensuel_median=row[16], loyer_mensuel_3_quartile=row[17], loyer_mensuel_9_decile=row[18], moyenne_loyer_mensuel=row[19], surface_moyenne=row[20], nombre_obsservations=row[21], nombre_logements=row[22], methodologie_production=row[23])
            loyer.save()

def reverse_func(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('loyers', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(import_csv, reverse_func),
    ]