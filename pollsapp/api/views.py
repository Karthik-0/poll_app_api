from rest_framework import generics
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from ..models import Question,Choice
from .serializers import QuestionSerializer,QuestionListSerializer

class QuestionListCreateView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionListSerializer
    # def perform_create(self, serializer):
        # choices = self.request
        # print(choices)
        # serializer.save(Choice=self.request.choice)
        # del request.data["calendarId"]
        # calendar = Calendar.objects.get(id=calendarId)
        # request.data["calendar"] = calendar
        # serializer = EventSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # return Response(serializer..errors, status=status.HTTP_400_BAD_REQUEST)

class QuestionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class VoteView(APIView):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(VoteView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        choice = request.data['choice']
        try:
            question = get_object_or_404(Question, pk=request.data['question_id'])
        except ValidationError:
            return JsonResponse({'data': 'not found'})
        try:
            selected_choice = question.choice.get(pk=choice)
        except (KeyError, Choice.DoesNotExist):
            return JsonResponse({'data': 'choice does not exist'})
        selected_choice.votes += 1
        selected_choice.save()
        return JsonResponse({'choice': request.data['choice'],'votes': selected_choice.votes})

class ResultView(APIView):
    def get(self,request,pk):
        try:
            question = get_object_or_404(Question, pk=pk)
        except ValidationError:
            return JsonResponse({'data': 'not found'})
        try:
            selected_choice = question.choice.filter(question=question)
        except (KeyError, Choice.DoesNotExist):
            return JsonResponse({'data': 'choice does not exist'})
        dic = {}
        li = [{choice.choice_text:choice.votes} for choice in selected_choice]

        # for choice in selected_choice:
            # dic['choice'] = choice.choice_text
            # dic['vote'] = choice.votes
            # li.append(dic)
        return JsonResponse({'data': li})
