from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Question
from django.template import loader


def index(request):

    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list' : latest_question_list,
    }
    return render( request, "polls/index.html", context)

    #3
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template ("polls/index.html")
    # context = {
    #     'latest_question_list' : latest_question_list,
    # }
    # return HttpResponse( template.render(context, request))
    
    #2
    #output = ', '.join(q.question_text for q in latest_question_list)
    #return HttpResponse(output)
    
    #1
    #return HttpResponse('Hello world! You are at the polls index')

def detail(request, question_id):

    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {'question': question})

    #2
    # try:
    #     question = Question.objects.get(pk = question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")

    # return render(request, "polls/detail.html", {'question': question})

    # 1
    # return HttpResponse("You are looking at question %s." % question_id)

def results(request, question_id):
    response = "You are looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
