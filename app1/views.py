from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app1_first(request):
    return HttpResponse('<h2>This is first view function of app1</h2>')

def app1_second(request):
    return HttpResponse('<h2><marquee>This is first view function of app1</marquee></h2>')
