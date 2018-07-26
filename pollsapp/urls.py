from django.conf.urls import url
from django.urls import  path
from .api import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('api/',view=views.QuestionListCreateView.as_view(),name = 'question_list_api'),
    path('api/<pk>',view=views.QuestionDetailView.as_view(),name = 'question_detail_api'),
    path('api/vote/',view=views.VoteView.as_view(),name="vote_view"),
    path('api/<pk>/results',view=views.ResultView.as_view(),name="vote_view"),
]
