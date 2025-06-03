from django.urls import path
from polls.views import index
from polls.views import detail
from polls.views import result
from polls.views import vote

app_name = 'polls'
urlpatterns = [
    path('', index, name='index'),
    path("<int:question_id>/", detail, name="detail"),
    path("<int:question_id>/result/", result, name="result"),
    path("<int:question_id>/vote/", vote, name="vote"),
]
