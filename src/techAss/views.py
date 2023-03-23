from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.
def home(request):
    template = loader.get_template('index.html')

    data = {"prenom":"Les Décodeuses"}

    return HttpResponse(template.render(data))