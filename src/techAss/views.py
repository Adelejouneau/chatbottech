from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import TechAssPages

# Create your views here.
def home(request):
    rsChatbotPage = ChatbotPage.objects.all()

    data = {
        "prenom":"Les Décodeuses",
        "chatbotPage": rsChatbotPage,
            }

    template = loader.get_template('index.html')
    return HttpResponse(template.render(data))

def chatbot(request):
    if request.GET.get("page"):
        rs = ChatbotPage.objects.get(title = request.GET["page"])
    else:
        rs = ChatbotPage.objects.get(title="")
        
    data = {'title': rs.title, "content": rs.content, "date": rs.date}

    template = loader.get_template("chatbot.html")
    return HttpResponse(template.render(data))


