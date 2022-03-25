from django.shortcuts import render
from django.http import HttpResponseRedirect

import requests

# Create your views here.

def index(request):
    return render(request, 'index.html')

def indexen(request):
    return render(request, 'index-en.html')    


def member(request):
    return render(request, 'member.html')        



def about(request):
    return render(request, 'about.html')         


def seo(request):
    return render(request, 'seo.html')    


def sosyal(request):
    return render(request, 'sosyal.html')    


def web(request):
    return render(request, 'web.html')    

def yazılım(request):
    return render(request, 'yazılım.html')                    