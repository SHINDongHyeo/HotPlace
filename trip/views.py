from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
import insta_crawl as ic



def index(request):
    return render(request, 'trip/index.html')


def insta_crawling(request):
    print("확인용")
    ic.setting()
    ic.crawling() # Model인 InstaHP클래스에 데이터 저장하는 함수 실행
    return render(request, 'trip/hotplace.html')