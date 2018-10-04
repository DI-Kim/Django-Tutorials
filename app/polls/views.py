from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from .models import Question


def index(request):
    # Question 클래스에 대한 QuerySet을 가져옴
    # 게시일자 속성에 대한 내림차순 순서로 최대 5개 까지
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }

    # 가져온 Question QuerySet을 사용, 각 Question의 question_text속성값들을
    # list comprehension을 사용해 리스트로 생성
    # 생성한 리스트를 ', ' 문자열의 join메서드의 인수로 전달, output에 쉼표단위로 연결된 문자열을 할당
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(template.render(context, request))
    return redirect('polls:index')

def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question does not exist')
    # 위의 4줄을 줄여 쓴 코드
    question = get_object_or_404(Question, pk=question_id)

    context = {
        'question': question
    }
    return render(request, 'polls/detail.html', context)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
