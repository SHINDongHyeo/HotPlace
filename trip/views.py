from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse("Hello, World. You're at the polls index.")


def index(request):
    return render(request, 'trip/index.html')

# def index(request):
#     # latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('trip/index.html')
#     context = {
#         # 'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))