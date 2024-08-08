from django.urls import path
from .views import *

urlpatterns = [
    path('', about.as_view(),name='about_modul')
]
