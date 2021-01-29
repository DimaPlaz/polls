from datetime import datetime

from rest_framework import generics

from .authentication import CsrfExemptSessionAuthentication
from .models import Poll, Question, QuestionChoice, Answer
from .serializers import PollSerializer, QuestionSerializer, AnswerSerializer


class PollsAPIView(generics.ListAPIView):
    serializer_class = PollSerializer
    queryset = Poll.objects.filter(start_date__lte=datetime.today(),
                                   end_date__gte=datetime.today())


class AnswersAPIView(generics.ListCreateAPIView):
    authentication_classes = (CsrfExemptSessionAuthentication,)
    serializer_class = AnswerSerializer

    def get_queryset(self):
        return Answer.objects.filter(
            question_id__poll_id=self.kwargs.get('poll_id'))

    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get("data", {}), list):
            kwargs["many"] = True

        return super(AnswersAPIView, self).get_serializer(*args, **kwargs)


class QuestionsAPIView(generics.ListAPIView):

    serializer_class = QuestionSerializer
    queryset = Question.objects.filter()
