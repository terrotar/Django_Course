from django.urls import path
from . import views


# It's a good practice to 'app_name = your_app_name'
# because like that Django will now that if there's
# another app with an index page, it will load the right
# one... Just need to put correctly in templates, like
# '{% url 'polls:index' argument_if_needed %}'
app_name = 'polls'
urlpatterns = [
    # Index_route = '/polls'
    # Before it was views.index, loading the function index of file views.py
    # and the parameter required was question_id...
    # Now, because of Django models, the parameter is a pk
    path('', views.IndexView.as_view(), name='index'),
    # Detail_route = '/polls/5'
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # Results_route = '/polls/5/results'
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # Vote_route = '/polls/5/vote'
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
