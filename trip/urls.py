from django.urls import path

from . import views

app_name = 'trip'
urlpatterns = [
    path('', views.index, name='index'),
    path('hotplace', views.insta_crawling, name='insta_crawling'),
]