from django.urls import path

from . import views

app_name = 'trip'
urlpatterns = [
    path('', views.index, name='index'),
    path('instacrawlsetting', views.insta_crawl_setting, name='insta_crawl_setting'),
    path('instacrawlcrawling', views.insta_crawl_crawling, name='insta_crawl_crawling'),
    path('hotplace', views.hotplace, name='hotplace'),
]