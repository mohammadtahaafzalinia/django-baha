from django.urls import path
from .views import *

urlpatterns = [
    path('',contactView.as_view(),name='contact_modul'),
]