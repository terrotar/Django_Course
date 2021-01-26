from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist.")
    return render(request, 'polls/detail.html', {'question': question})
# You can try too the function of 'django.http' called 'get_object_or_404'.
# question = get_object_or_404(Question, pk=question_id)


def results(request, question_id):
    response = f"You are looking at the results of question {question_id}."
    return HttpResponse(response)


def vote(request, question_id):
    return HttpResponse(f"You are voting on question {question_id}.")
