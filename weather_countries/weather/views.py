import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.template.defaultfilters import slugify
from requests import get
from datetime import *
from django.views.generic import *
import pytz
from translate import Translator
from weather.models import Weather_Country


# Create your views here.
def home(request):
    return render(request,'weather/home.html')
class Search(DetailView,Translator):
    template_name = 'weather/home.html'
    context_object_name = 'weather'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        translater = Translator(from_lang='en',to_lang='ru')
        try:
            url = self.request.GET.get('q')
            responce = get(f'http://api.weatherapi.com/v1/current.json?key=9ab64eef200c4afaa5180041232209&q={url.title()}').json()
            location = responce['location']['tz_id']
            now = pytz.timezone(location)
            time1 = datetime.now(now).strftime("%T")
            now = pytz.timezone(location)
            morning = datetime(2023, 10, 6) + timedelta(hours=4)
            morning2 = datetime(2023, 10, 9) + timedelta(hours=12)
            afternoon = datetime(2023, 10, 9) + timedelta(hours=17)
            evening = datetime(2023, 10, 9) + timedelta(hours=23)
            night = datetime(2023, 10, 9)
            context['time'] = translater.translate(datetime.now(now).strftime("%d %A %B %Y %T"))
            context['time2'] = datetime.now(now).time()
            context['if_time'] = morning.time()
            context['if_time2'] = morning2.time()
            context['afternoon'] = afternoon.time()
            context['evening'] = evening.time()
            context['night'] = night.time()
            context['time'] = translater.translate(time1)
        except:
            ...
        return context
    def get_object(self):
        translater = Translator(from_lang='en', to_lang='ru')
        translater2 = Translator(from_lang='ru', to_lang='en')
        Weather_Country.objects.all().delete()
        url = self.request.GET.get('q')
        try:
            responce = get(f'http://api.weatherapi.com/v1/current.json?key=9ab64eef200c4afaa5180041232209&q={url.title()}').json()
            name = responce['location']['name']
            region = responce['location']['region']
            country = responce['location']['country']
            temp = responce['current']['temp_c']
            description = responce['current']['condition']['text']
            description2 = translater.translate(description)
            icon_description = responce['current']['condition']['icon']
            wind_speed_kph = responce['current']['wind_kph']
            wind_speed_mph = responce['current']['wind_mph']
            humidity = responce['current']['humidity']
            gust_kph = responce['current']['gust_kph']
            gust_mph = responce['current']['gust_mph']
            name2 = translater2.translate(name)
            if name.lower() == 'илулисcат':
                name2 = 'ilulissat'
            Weather_Country.objects.create(name=name,region=region,country=country,temp=temp,descriprion=description2,icon_desc=icon_description,wind_speed_kph=wind_speed_kph,wind_speed_mph=wind_speed_mph,humidity=humidity,gust_kph=gust_kph,gust_mph=gust_mph,slug=slugify(name2))
            return Weather_Country.objects.get(name__istartswith=self.request.GET.get('q').title())
        except:
            return 'Такого города нет!'
class MorePage(DetailView):
    model = Weather_Country
    template_name = 'weather/more.html'
    context_object_name = 'weather'
    slug_url_kwarg = 'weath_name'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        translater = Translator(from_lang='en',to_lang='ru')
        url = Weather_Country.objects.all()[0]
        responce = get(f'http://api.weatherapi.com/v1/current.json?key=9ab64eef200c4afaa5180041232209&q={url}').json()
        location = responce['location']['tz_id']
        now = pytz.timezone(location)
        morning = datetime(2023,10,6) + timedelta(hours=4)
        morning2 = datetime(2023,10,9) + timedelta(hours=12)
        afternoon = datetime(2023,10,9) + timedelta(hours=18)
        evening = datetime(2023,10,9) + timedelta(hours=23)
        night = datetime(2023,10,9)
        afternoon2 = datetime(2023, 10, 9) + timedelta(hours=18, minutes=30)
        context['time'] = translater.translate(datetime.now(now).strftime("%d %A %B %Y %T"))
        context['time2'] = datetime.now(now).time()
        context['if_time'] = morning.time()
        context['if_time2'] = morning2.time()
        context['afternoon'] = afternoon.time()
        context['evening'] = evening.time()
        context['afternoon2'] = afternoon2.time()
        context['night'] = night.time()
        context['title'] = context['weather']
        return context
    def get_object(self, queryset=None):
        return Weather_Country.objects.get(slug=self.kwargs['weath_name'])
    