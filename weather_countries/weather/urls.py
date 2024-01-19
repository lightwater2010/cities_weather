from django.urls import path
from django.views.decorators.cache import cache_page

from weather.views import *

urlpatterns = [
    path('',home,name='home'),
    path('search/',Search.as_view(),name='search'),
    path('more/<slug:weath_name>',MorePage.as_view(),name='more')
]