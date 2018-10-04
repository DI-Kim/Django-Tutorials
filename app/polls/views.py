from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from .models import Question, Choice


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
    return render(request, 'polls/index.html', context)

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
    #question_id가 pk인 Question객체를 DB로 부터 가져온 데이터로 생성
    #만약 해당하는 Question이 없다면 Http404예외가 발생함
    question = get_object_or_404(Question, pk = question_id)
    try:
        #현재 투표중인 Question에 속한 Choice목록에서
        # pk가 POST요청에 전달된 'choice'값에 해당하는 Choice객체를 selected_choice변수에 할당
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        #위의 try문에서 발생할 수 있는 예외는 2가지
        # 1. KeyError:              request.POST에 'choice'키가 없을때 발생
        # 2. Choice.DoesNotExist:   .get(pk=어떤값)에서 발생 (pk에 해당하는 객체가 DB에 없을 경우)
        context = {
            'qeustion': question,
            'error_message': "You didn't select a choice."
        }
        return render(request, 'polls/detail.html', context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return redirect('polls:results', question_id)
