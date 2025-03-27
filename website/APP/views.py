from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html') #http://127.0.0.1:8000/home/


def test(request):
    return render(request, 'test.html')

def museum(requests):
    return render(requests, 'museum.html')

def monuments(requests):
    return render(requests, 'monuments.html')

def interesting_location(requests):
    return render(requests, 'interesting_location.html')