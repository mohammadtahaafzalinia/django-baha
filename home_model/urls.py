from django.urls import path
from .views import *
import uuid
urlpatterns = [
    path('',home.as_view(),name='home'),
    path('page404/',http_404,name='res_404'),
    path(f'{unique_id1}',link,name='link'),
    path(f'{unique_id2}',js,name='js'),
    path(f'{unique_id3}',theme_options,name='theme'),
    path(f'{unique_id4}',preloader,name='preloader'),
    path(f'{unique_id5}',main_site,name='main_site'),
    path(f'{unique_id6}',Home_section,name='home_section'),
    path(f'{unique_id7}',menu,name='menu'),
    path(f'{unique_id8}',play_music, name='play_music'),
    # path('/<code>',home_lan.as_view(), name='home_lan'),

]
