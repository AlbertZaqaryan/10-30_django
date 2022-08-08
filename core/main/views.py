from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('Hello My team')


def about(request):
    return HttpResponse('About us page')