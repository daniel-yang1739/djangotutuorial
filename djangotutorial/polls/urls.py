from django.urls import path
from polls.views import index
from polls.views import details
from polls.views import results
from polls.views import vote

urlpatterns = [
    path('', index, name='index'),
    path("<int:question_id>/", details, name="details"),
    path("<int:question_id>/results/", results, name="results"),
    path("<int:question_id>/vote/", vote, name="vote"),
]
