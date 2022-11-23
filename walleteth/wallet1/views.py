from django.shortcuts import render
from django.template.response import TemplateResponse
from django.http import HttpResponse
# Create your views here.
##def index(request):
    ##return render(request, "index.html")
##from .models import #Book, Author, BookInstance, Genre

def index(request):
    return render(request, 'index.html')

def status(request):
    return HttpResponse()
