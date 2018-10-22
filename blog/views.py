from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('HELLO WORLD')


def about(response):
    return HttpResponse('ABOUT PAGE')
