from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html') #http://127.0.0.1:8000/home/
