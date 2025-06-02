from django.http import HttpResponse
from django.shortcuts import render
from polls.models import Question


def index(request):
    template = 'polls/index.html'
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request, template, context)


def details(request, question_id):
    response = f"You're looking at the details of question {question_id}"
    return HttpResponse(response)


def results(request, question_id):
    response = f"You're looking at the results of question {question_id}."
    return HttpResponse(response)


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")
