from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

# Create your views here.
def home(request):
    template = loader.get_template('index.html')
    data = {"prenom":"Les Décodeuses"}

    return HttpResponse(template.render(data))


