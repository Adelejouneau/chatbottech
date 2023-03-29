from django.shortcuts import render
from .models import Question
# Create your views here.

def chatbot_view(request):
    questions = Question.objects.all()
    return render(request, "chatbot.html", {"questions": questions})