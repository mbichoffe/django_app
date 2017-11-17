from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Question
# Create your views here.



def index(request):
    """Display the latest 5 poll questions in the system 
        according to publication date
    """
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    """Displays a question text, with no results but with a form to vote."""
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/details.html', {'question': question})


def results(request, question_id):
    """Displays results for a particular question."""
    response = "You're looking at the results of question {}".format(question_id)
    return HttpResponse(response)


def vote(request, question_id):
    """Handles voting for a particular choice in a particular question."""
    return HttpResponse("You\'re voting on question {}".format(question_id))
