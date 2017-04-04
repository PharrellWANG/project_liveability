from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Scores(models.Model):
    district_en = models.CharField(max_length=45, null=True)
    district_ch = models.CharField(max_length=45, null=True)
    score_of_liveability = models.IntegerField(null=True)
    house_cost = models.IntegerField(null=True)
    dining_cost = models.IntegerField(null=True)
    crime_rate = models.IntegerField(null=True)
    edu_rank = models.IntegerField(null=True)
    real_crime_rate = models.FloatField(null=True)
    # house_cost = models.IntegerField()


class TwoDishesOneSoupIdx(models.Model):
    district_en = models.CharField(max_length=45, null=True)
    district_ch = models.CharField(max_length=45, null=True)
    source_street_chn_name = models.CharField(max_length=45, null=True)
    ave_price = models.FloatField(null=True)


class HousePricePerSquareInch(models.Model):
    district_en = models.CharField(max_length=45, null=True)
    district_ch = models.CharField(max_length=45, null=True)
    # source_street_chn_name = models.CharField(max_length=45, null=True)
    ave_price = models.FloatField(null=True)


class PriSchoolRank(models.Model):
    # rank_on_web = models.IntegerField(null=True)
    name_of_school = models.CharField(max_length=50, null=True)
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)
    academic = models.CharField(max_length=10, null=True)
    sport = models.CharField(max_length=40, null=True)
    music = models.CharField(max_length=10, null=True)
    teaching_resource = models.CharField(max_length=10, null=True)
    dormitory = models.CharField(max_length=10, null=True)
    ranking_score_this_year = models.CharField(max_length=10, null=True)
    ranking_score_average = models.CharField(max_length=10, null=True)
    district_chn = models.CharField(max_length=10, null=True)
    district_eng = models.CharField(max_length=50, null=True)


class MidSchoolRank(models.Model):
    # rank_on_web = models.IntegerField(null=True)
    name_of_school = models.CharField(max_length=50, null=True)
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)
    academic = models.CharField(max_length=10, null=True)
    sport = models.CharField(max_length=40, null=True)
    music = models.CharField(max_length=10, null=True)
    teaching_resource = models.CharField(max_length=10, null=True)
    dormitory = models.CharField(max_length=10, null=True)
    ranking_score_this_year = models.CharField(max_length=10, null=True)
    ranking_score_average = models.CharField(max_length=10, null=True)
    district_chn = models.CharField(max_length=10, null=True)
    district_eng = models.CharField(max_length=50, null=True)


class PopulationAndArea(models.Model):
    district_ch = models.CharField(max_length=10, null=True)
    district_en = models.CharField(max_length=50, null=True)
    population = models.IntegerField(null=True)
    area = models.FloatField(null=True)


class Employment(models.Model):
    district_ch = models.CharField(max_length=10, null=True)
    district_en = models.CharField(max_length=50, null=True)
    median_monthly_household_income = models.FloatField(null=True)
    poverty_rate = models.FloatField(null=True)


class Weather(models.Model):
    district_ch = models.CharField(max_length=10, null=True)
    district_en = models.CharField(max_length=50, null=True)
    air_quality_health_index = models.FloatField(null=True)
