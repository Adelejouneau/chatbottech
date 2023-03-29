from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import TechAssPages

# Create your views here.
def home(request):
    rsChatbotPage = TechAssPages.objects.all()
    data = {
        "page" :'detail',
        "prenom":"Les Décodeuses",
        "chatbotPage": rsChatbotPage,
    }
    template = loader.get_template('index.html')
    return HttpResponse(template.render(data))

def chatbot(request):
    data = {'page': 'chatbot',}
    template = loader.get_template("index.html")
    return HttpResponse(template.render(data))


