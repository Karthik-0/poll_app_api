from rest_framework import generics

from ..models import Question,Choice
from .serializers import QuestionSerializer

class QuestionListCreateView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer