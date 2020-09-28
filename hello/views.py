from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'hello/index.html')

def nweni(request):
    return HttpResponse("hello nweni")

def painglay(request):
    return HttpResponse("hello painglay")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })
