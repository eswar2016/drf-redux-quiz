from django.shortcuts import render
from rest_framework import routers, serializers, viewsets

from .models import Question
from .serializers import QuestionSerializer
# Create your views here.


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer