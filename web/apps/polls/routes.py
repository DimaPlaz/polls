from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import PollsAPIView, AnswersAPIView, QuestionsAPIView


urlpatterns = [
    path('polls/', PollsAPIView.as_view()),
    path('polls/<int:poll_id>/answers/', csrf_exempt(AnswersAPIView.as_view())),
    path('polls/<int:poll_id>/questions/', QuestionsAPIView.as_view()),
]