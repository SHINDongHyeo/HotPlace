from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
import insta_crawl as ic
import analyze as az
from .models import InstaHP



def index(request):
    return render(request, 'trip/index.html')

def insta_crawl_setting(request):
    result = "fail"
    try:
        ic.insta.setting()
        result = "success"
        print(result)
    except:
        print(result)
    return HttpResponse(result)
    

def insta_crawl_crawling(request):
    print("크롤링시작-----------------------------------------------")
    keyword = request.GET.get('keyword')
    number_of_posts = request.GET.get("number_of_posts")
    print('검색할태그 : ',keyword)
    print('검색할게시물수 : ',number_of_posts)
    ic.insta.crawling(keyword,number_of_posts) # Model인 InstaHP클래스에 데이터 저장하는 함수 실행
    print("크롤링끝-----------------------------------------------")
    return HttpResponse("result")
    # render(request, 'trip/hotplace.html')

def hotplace(request):
    print("hotplace---------------------------------------------------------------------")
    data = InstaHP.objects.all()
    result = az.solution(data)
    context = {"result":result}
    return render(request, 'trip/hotplace.html',context)