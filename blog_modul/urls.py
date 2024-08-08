from django.urls import path
from .views import *


urlpatterns = [
    path('',blog_view.as_view(),name='blog'),
    path('list',blogList_view.as_view(),name='blog_list'),
    path('<slug:slug>',blogDitail_view.as_view(),name='blog_ditail'),
    path('category/<cat>/',blog_cat,name='blog_cat'),
    path('search/',blog_search.as_view(),name='blog_search'),
    path('add-comment/',blog_comment,name='blog_comment')

]