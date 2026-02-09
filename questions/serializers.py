from rest_framework import serializers
from .models import Question

class QuestionSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='external_id')

    class Meta:
        model = Question
        fields = [
            'id',
            'category',
            'question_text',
            'options',
            'correct_answer',
            'explanation_tr',
        ]
