# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-10 07:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loyers', '0006_auto_20160710_0721'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loyer',
            name='Observatory',
        ),
        migrations.RemoveField(
            model_name='loyer',
            name='Type_habitat',
        ),
        migrations.RemoveField(
            model_name='loyer',
            name='Zone_complementaire',
        ),
        migrations.RemoveField(
            model_name='loyer',
            name='agglomeration',
        ),
        migrations.RemoveField(
            model_name='loyer',
            name='anciennete_locataire_homogene',
        ),
        migrations.RemoveField(
            model_name='loyer',
            name='epoque_construction_homogene',
        ),
        migrations.RemoveField(
            model_name='loyer',
            name='methodologie_production',
        ),
        migrations.RemoveField(
            model_name='loyer',
            name='nombre_pieces_homogene',
        ),
    ]
