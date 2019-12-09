from django.shortcuts import render
from  django.http import HttpResponse
# Create your views here.

def index(request):         # dinh nghia ham
    return HttpResponse('Hello World')
