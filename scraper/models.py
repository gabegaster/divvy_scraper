from django.db import models

class Hit(models.Model):
    execution_time = models.DateTimeField("time scraped")

class Station(models.Model):
    hit = models.ForeignKey(Hit)
    available_bikes = models.IntegerField(default=0)
    available_docks = models.IntegerField(default=0)
    city = models.CharField(max_length=100)
    bean_id = models.IntegerField(default=0)
    landmark = models.CharField(max_length=100, default="")
    latitude = models.FloatField(default=0)
    location =  models.CharField(max_length=200)
    longitude = models.FloatField(default=0)
    stAddress = models.CharField(max_length=200)
    station_name= models.CharField(max_length=200)
    status_key = models.IntegerField(default=0)
    status_value = models.CharField(max_length=200)
    test_station = models.BooleanField(default=0)
    total_docks = models.IntegerField(default=0)
