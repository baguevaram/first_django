#from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def p1(request):
    return HttpResponse("Test for the poll number 1")

