from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
# Create your views here.



def index(request):
    """Display the latest 5 poll questions in the system 
        according to publication date
    """
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


def detail(request, question_id):
    """Displays a question text, with no results but with a form to vote."""
    return HttpResponse("You're looking at question {}".format(question_id))


def results(request, question_id):
    """Displays results for a particular question."""
    response = "You're looking at the results of question {}".format(question_id)
    return HttpResponse(response)


def vote(request, question_id):
    """Handles voting for a particular choice in a particular question."""
    return HttpResponse("You\'re voting on question {}".format(question_id))
