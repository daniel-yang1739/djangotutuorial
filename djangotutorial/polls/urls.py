from django.urls import path
from polls.views import IndexView
from polls.views import DetailView
from polls.views import ResultView
from polls.views import vote

app_name = 'polls'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path("<int:pk>/", DetailView.as_view(), name="detail"),
    path("<int:pk>/result/", ResultView.as_view(), name="result"),
    path("<int:question_id>/vote/", vote, name="vote"),
]
