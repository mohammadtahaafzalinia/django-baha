from django.urls import path
from .views import *

urlpatterns = [
    path('',Portfolio_view.as_view(),name='portfolio'),
    path('<slug:slug>/',Video_view.as_view(),name='video'),

]