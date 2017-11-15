from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world, You're at the polls index.")

def detail(request, question_id):
    "displays a question text, with no results but with a form to vote."
    return HttpResponse("You're looking at question {}".format(question_id))

def results(request, question_id):
    "displays results for a particular question."
    response = "You're looking at the results of question {}".format(question_id)
    return HttpResponse(response)

def vote(request,question_id):
    "handles voting for a particular choice in a particular question."
    return HttpResponse("You\'re voting on question {}".format(question_id))
    