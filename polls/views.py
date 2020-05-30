from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from .models import Question

def index(request):
    template_name = 'polls/index.html'

    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}

    return render(request, template_name, context)

def detail(request, question_id):
    template_name = 'polls/detail.html'

    try:
        question = Question.objects.get(pk=question_id)
        context = {'question': question}
    except Question.DoesNotExist:
        raise Http404("Question does not exist")

    return render(request, template_name, context)

def results(request, question_id):
    response = f"You're looking at the results of question {question_id}."
    return HttpResponse(response)

def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")