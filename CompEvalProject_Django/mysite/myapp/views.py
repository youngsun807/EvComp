from django.shortcuts import render
import json

# Create your views here.
from .models import Question, Choice

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

# http://127.0.0.1:8000/myapp
def index(request):
    print("---------index()-------------")
    #QuerySet 타입의 객체로 반환
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    print(latest_question_list)
    context = {'latest_question_list': latest_question_list}
    return render(request, 'myapp/index.html', context)

# http://127.0.0.1:8000/myapp/2/
def detail(request, question_id):
    print("---------detail()------------- ", question_id)
    #Question 타입반환
    question = get_object_or_404(Question, pk=question_id)
    print("*** detail() : 변수 타입 ", type(question))#Question 
    print("*** detail() : 변수 값 ", question)#Question 객체의 __str__ 함수반환값    
    return render(request, 'myapp/detail.html', {'question' : question})

# http://127.0.0.1:8000/myapp/2/results/
def vote(request, question_id):
    print("---------vote()-------------")
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'myapp/detail.html', {'question':question, 'error_message' : '선택 불가입니다'})
    selected_choice.votes += 1
    selected_choice.save()
    # http://127.0.0.1:8000/myapp/2/results/
    return HttpResponseRedirect(reverse('myapp:results', args=(question.id,)))

# http://127.0.0.1:8000/myapp/2/results/
# 폼 데이터 처리 결과를 보여주는 로직
def results(request, question_id):
    print("---------results()-------------")
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'myapp/results.html', {'question':question})


#json 형태의 문자열로 응답 : 비동기
def ajaxRes(request):
    print("----- ajaxRes() -----")
    context = {'message': "비동기로 응답하는 데이터", 'age' : 20, 'like_count': 10, 'data':"['Task', 'Hours per Day'],['Work',     11],['Eat',      2],['Commute',  2],['Watch TV', 2],['Sleep',    7]"}
    return HttpResponse(json.dumps(context), content_type="application/json")



'''
* mysite/urls.py
    
urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', views.index, name='index'),
    path('myapp/<int:question_id>/', views.detail, name='detail'),
    path('myapp/<int:question_id>/results', views.results, name='results'),
    path('myapp/<int:question_id>/vote', views.vote, name='vote'),
]

'''