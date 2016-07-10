from __future__ import unicode_literals

from django.db import models


class Observatory(models.Model):
    name = models.CharField(max_length=255)
    def __unicode__(self):
        return self.name


class Agglomeration(models.Model):
    name = models.CharField(max_length=255)
    def __unicode__(self):
        return self.name


class AgglomerationDescription(models.Model):
    name = models.CharField(max_length=255)
    def __unicode__(self):
        return self.name


class HousingType(models.Model):
    name = models.CharField(max_length=255)
    def __unicode__(self):
        return self.name


class ConstructionPeriod(models.Model):
    name = models.CharField(max_length=255)
    def __unicode__(self):
        return self.name


class RenterSeniority(models.Model):
    name = models.CharField(max_length=255)
    def __unicode__(self):
        return self.name


class NumberOfRooms(models.Model):
    name = models.CharField(max_length=255)
    def __unicode__(self):
        return self.name


class ProductionMethodology(models.Model):
    name = models.CharField(max_length=255)
    def __unicode__(self):
        return self.name


class Loyer(models.Model):
    observatory = models.ForeignKey('Observatory', null=True)
    year = models.IntegerField(max_length=200)
    agglomeration = models.ForeignKey('Agglomeration', null=True)
    agglomeration_description = models.ForeignKey('AgglomerationDescription', null=True)
    housing_type = models.ForeignKey('HousingType', null=True)
    construction_period = models.ForeignKey('ConstructionPeriod', null=True)
    renter_seniority = models.ForeignKey('RenterSeniority', null=True)
    number_of_rooms = models.ForeignKey('NumberOfRooms', null=True)
    loyer_1_decile = models.FloatField(max_length=200, null=True)
    loyer_1_quartile = models.FloatField(max_length=200, null=True)
    loyer_median = models.FloatField(max_length=200, null=True)
    loyer_3_quartile = models.FloatField(max_length=200, null=True)
    loyer_9_decile = models.FloatField(max_length=200, null=True)
    loyer_moyen = models.FloatField(max_length=200, null=True)
    loyer_mensuel_1_decile = models.IntegerField(max_length=200, null=True)
    loyer_mensuel_1_quartile = models.IntegerField(max_length=200, null=True)
    loyer_mensuel_median = models.IntegerField(max_length=200, null=True)
    loyer_mensuel_3_quartile = models.IntegerField(max_length=200, null=True)
    loyer_mensuel_9_decile = models.IntegerField(max_length=200, null=True)
    moyenne_loyer_mensuel = models.IntegerField(max_length=200, null=True)
    loyer_moyen = models.IntegerField(max_length=200, null=True)
    nombre_obsservations = models.IntegerField(max_length=200, null=True)
    nombre_logements = models.IntegerField(max_length=200, null=True)
    production_methodology = models.ForeignKey('ProductionMethodology', null=True)
