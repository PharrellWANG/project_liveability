from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Scores(models.Model):
    district_en = models.CharField(max_length=45, null=True)
    district_ch = models.CharField(max_length=45, null=True)
    house_cost = models.IntegerField(null=True)
    dining_cost = models.IntegerField(null=True)
    crime_rate = models.IntegerField(null=True)
    edu_rank = models.IntegerField(null=True)
    # house_cost = models.IntegerField()


class TwoDishesOneSoupIdx(models.Model):
    district_en = models.CharField(max_length=45, null=True)
    district_ch = models.CharField(max_length=45, null=True)
    source_street_chn_name = models.CharField(max_length=45, null=True)
    ave_price = models.FloatField(null=True)
