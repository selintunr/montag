from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages

import requests

from webPage1.models import staticAboutModel,staticAboutModel2,referansi,referansi2
from webPage1.forms import contactForm, subForm,contactForm2, subForm2



def index(request):
    context = dict()


    context['form'] = contactForm()
    context['subForm'] = subForm()
    context['refer'] = referansi.objects.all()

    if request.method == "POST":
        form = contactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        context['form'] = contactForm()
        return render(request, "index.html", context)



        

    if request.method == "POST":
        form = subForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        context['form'] = subForm()
        
        return render(request, "index.html", context)
    return render(request, 'index.html', context)






def indexen(request):
    context = dict()


    context['form'] = contactForm2()
    context['subForm'] = subForm2()
    context['refer'] = referansi2.objects.all()

    if request.method == "POST":
        form = contactForm2(request.POST)
        if form.is_valid():
            form.save()
            return redirect('indexen')
    else:
        context['form'] = contactForm()
        return render(request, "index-en.html", context)

    if request.method == "POST":
        form = subForm2(request.POST)
        if form.is_valid():
            form.save()
            return redirect('indexen')
    else:
        context['form'] = subForm()
        
        return render(request, "index-en.html", context)
    return render(request, 'index-en.html', context)
   


def member(request):
    return render(request, 'member.html')        



def about(request):   
    context = dict()
    a = staticAboutModel.objects.all()
    print("----------------------", a)
    context['about'] = staticAboutModel.objects.all()

    return render(request, 'about.html', context)   


def hizmet(request):   
    context = dict()
    a = staticAboutModel.objects.all()
    print("----------------------", a)
    context['hizmet'] = staticAboutModel.objects.all()

    return render(request, 'hizmet.html', context)             


def seo(request):
    return render(request, 'seo.html')    


def sosyal(request):
    return render(request, 'sosyal.html')    


def web(request):
    return render(request, 'web.html')    

def yazılım(request):
    return render(request, 'yazılım.html')                    