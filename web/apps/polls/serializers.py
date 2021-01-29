from rest_framework import serializers

from .models import Poll, Question, QuestionChoice, Answer


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = '__all__'


# class QuestionChoiceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = QuestionChoice
#         fields = ('choice',)


class QuestionSerializer(serializers.ModelSerializer):
    choices = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = '__all__'

    def get_choices(self, obj):
        return QuestionChoice.objects.filter(
            question_id=obj.id
        ).values_list('choice', flat=True)


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
