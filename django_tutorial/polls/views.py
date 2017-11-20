from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Choice, Question
from django.db.models import F
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

class DetailsView(generic.DetailView):
    model = Question
    template_name = 'polls/details.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


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
        selected_choice.votes = F('votes') + 1
        """
        Although reporter.stories_filed = F('stories_filed') + 1 looks like
        a normal Python assignment of value to an instance attribute, in fact
        it’s an SQL construct describing an operation on the database.
        When Django encounters an instance of F(), it overrides the standard
        Python operators to create an encapsulated SQL expression; in this case, 
        one which instructs the database to increment the database field
        represented by reporter.stories_filed.

        Whatever value is or was on reporter.stories_filed, Python never gets
        to know about it - it is dealt with entirely by the database.
        All Python does, through Django’s F() class, is create the SQL
        syntax to refer to the field and describe the operation
        """
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing with
        # POST data. This prevents data from being posted twice if a
        #user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
