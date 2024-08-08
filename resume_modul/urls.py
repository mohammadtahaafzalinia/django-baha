from django.urls import path
from .views import *


urlpatterns = [
    path('',resume_view.as_view(),name='resume')
]