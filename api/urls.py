"""URL Configuration"""

from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('',index_view,name='index'),
    path('api/transfer/', Transfer.as_view(), name='transfer'),
    path('api/details/', Details.as_view(), name='transfer'),
]