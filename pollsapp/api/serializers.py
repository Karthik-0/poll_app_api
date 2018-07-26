from rest_framework import serializers
from ..models import Question,Choice

class QuestionSerializer(serializers.ModelSerializer):
    # choice = serializers.RelatedField(many=True)
    choice = serializers.StringRelatedField(many=True)
    class Meta:
        model = Question
        fields = ['question_text','pub_date','uuid','choice']