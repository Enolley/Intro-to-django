from django.http import HttpResponse
from django.shortcuts import render


def Home(request):
    return HttpResponse("Web development class")

def about(request):
    return HttpResponse("About")

def services(request):
    return HttpResponse("Services")
