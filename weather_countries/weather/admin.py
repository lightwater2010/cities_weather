from django.contrib import admin

from weather.models import Weather_Country


# Register your models here.
class WeatherAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Weather_Country,WeatherAdmin)