from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import TechAssPages
from django.db.models import Q

# Create your views here.

# VIEWS HOME
def home(request):
    rsChatbotPage = TechAssPages.objects.all()
    data = {
        "page" :'detail',
        "chatbotPage": rsChatbotPage,
    }
    template = loader.get_template('index.html')
    return HttpResponse(template.render(data))

# VIEWS CHATBOT
def chatbot(request):
    data = {'page': 'chatbot',}
    template = loader.get_template("index.html")
    return HttpResponse(template.render(data))

# VIEWS CONTACT
def contact(request):
    rsChatbotPage = list(TechAssPages.objects.filter(title="contact").values('content'))
    data = {
        "page" :'contact',
        "infos": rsChatbotPage[0]['content'],
    }

    template = loader.get_template("index.html")
    return HttpResponse(template.render(data))

# VIEWS SERVICE
def service(request):
    rsChatbotPage = list(TechAssPages.objects.filter(title="service").values('content'))
    data = {
        "page" :'service',
        "infos": rsChatbotPage[0]['content'],
    }

    template = loader.get_template("index.html")
    return HttpResponse(template.render(data))

# def service(request):
#     rsChatbotPage = list(TechAssPages.objects.filter(title="cybersecurite").values('content'))
#     data = {
#         "page" :'cybersecurite',
#         "infos": rsChatbotPage[0]['content'],
#     }

#     template = loader.get_template("index.html")
#     return HttpResponse(template.render(data))

# VIEWS LOGICIEL
def logiciel(request):
    rsChatbotPage = list(TechAssPages.objects.filter(title="logiciel").values('content'))
    data = {
        "page" :'logiciel',
        "infos": rsChatbotPage[0]['content'],
    }
    template = loader.get_template("index.html")
    return HttpResponse(template.render(data))
