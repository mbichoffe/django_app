from django.conf.urls import url

from . import views
app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailsView.as_view(), name='details'),
    # ex: /polls/5/results
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name="results"),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

# note about regex
# (?P<name>regex)
# Captures the text matched by "regex" into the group "name".
# The name can contain letters and numbers but must start with a letter.
# the Named capturing group 'question_id' matches a set of chars in the range
# of 0-9 (indicated by the square brackets and -)

]
