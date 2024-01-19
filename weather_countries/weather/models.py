
from django.db import models
from django.urls import reverse


# Create your models here.
class Weather_Country(models.Model):
    name = models.CharField(max_length=100)
    region = models.TextField()
    country = models.CharField(max_length=100)
    temp = models.FloatField()
    descriprion = models.TextField()
    icon_desc = models.TextField()
    wind_speed_kph = models.FloatField()
    wind_speed_mph = models.FloatField()
    humidity = models.FloatField()
    gust_kph = models.FloatField()
    gust_mph = models.FloatField()
    slug = models.SlugField(default=True)
    def __str__(self):
        return self.name
    def get_absolute_urls(self):
        return reverse('more',kwargs={'weath_name':self.slug})