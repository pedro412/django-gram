from platzigram.views import hello_world, sort_integers, say_hi
from django.contrib import admin
from django.http.response import HttpResponse
from django.urls import path


urlpatterns = [
    path('hello-world/', hello_world),
    path('sorted/', sort_integers),
    path('hi/<str:name>/<int:age>/', say_hi)
]
