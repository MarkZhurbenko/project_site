"""
URL configuration for website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from APP.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name='home'), #http://127.0.0.1:8000/home/
    path('test/', test, name='test'), #http://127.0.0.1:8000/test/
    path('museum/', museum, name='museum'), #http://127.0.0.1:8000/home/museum/
    path('monuments/', monuments, name='monuments'), #http://127.0.0.1:8000/home/monuments/
    path('interesting_location', interesting_location, name='interesting_location'), #http://127.0.0.1:8000/home/interesting_location
    
]
