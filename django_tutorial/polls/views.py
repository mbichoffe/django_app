from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Choice, Question
# Create your views here.



def index(request):
    """Display the latest 5 poll questions in the system 
        according to publication date
    """
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def details(request, question_id):
    """Displays a question text, with no results but with a form to vote."""
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/details.html', {'question': question})


def results(request, question_id):
    """Displays results for a particular question."""
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    """Handles voting for a particular choice in a particular question."""
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        #redisplay the question voting form
        return render(request, 'polls/details.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing with
        # POST data. This prevents data from being posted twice if a
        #user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
