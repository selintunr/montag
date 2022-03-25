"""datamontagweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from root import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('indexen/',views.indexen,name='indexen'),
    path('member/',views.member,name='member'),
    path('about/',views.about,name='about'),
    path('seo/',views.seo,name='seo'),
    path('sosyal/',views.sosyal,name='sosyal'),
    path('web/',views.web,name='web'),
    path('yazılım/',views.yazılım,name='yazılım'),
]