# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-10 13:02
from __future__ import unicode_literals

from django.db import migrations


def merge_number_of_rooms(apps, schema_editor):
    # MODE BOURRIN
    NumberOfRooms = apps.get_model("loyers", "NumberOfRooms")
    Loyer = apps.get_model("loyers", "Loyer")
    loyers = Loyer.objects.all()
    for loyer in loyers:
        if loyer.number_of_rooms_id == 10:
            loyer.number_of_rooms_id = 6
        if loyer.number_of_rooms_id == 9:
            loyer.number_of_rooms_id = 5
        if loyer.number_of_rooms_id == 8:
            loyer.number_of_rooms_id = 4
        if loyer.number_of_rooms_id == 7 or loyer.number_of_rooms_id == 3:
            loyer.number_of_rooms_id = 2
    number_of_rooms = NumberOfRooms.objects.filter(id__in=[10, 9, 8, 7, 3])
    number_of_rooms.delete()


def reverse_func(apps, schema_editor):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('loyers', '0010_auto_20160710_1250'),
    ]

    operations = [
        migrations.RunPython(merge_number_of_rooms, reverse_func),
    ]
