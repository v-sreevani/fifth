from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def first_app2(request):
    return HttpResponse('<h1><marquee> this is my second app2 function</marquee></h1>')

def second_app2(request):
    return HttpResponse('<h1>this is my second app2 function</h1>' )
