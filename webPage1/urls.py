from django.contrib import admin
from django.urls import path
from . import views

app_name = "webPage1"

urlpatterns = [
    path('indexen/',views.indexen,name='indexen'),
    path('member/',views.member,name='member'),
    path('seo/',views.seo,name='seo'),
    path('sosyal/',views.sosyal,name='sosyal'),
    path('web/',views.web,name='web'),
    path('yazılım/',views.yazılım,name='yazılım'),
    path('hizmet/',views.hizmet,name='hizmet'),

]
