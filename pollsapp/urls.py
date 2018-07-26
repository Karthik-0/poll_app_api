from django.conf.urls import url
from django.urls import  path
from .api import views

urlpatterns = [
    path('api/',view=views.QuestionListCreateView.as_view(),name = 'question_list_api'),
]
