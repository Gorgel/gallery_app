from django.shortcuts import render
from models import Picture
# Create your views here.

def index(request):

    pictures = Picture.objects.filter()
    context = {'pictures' : pictures }

    return render(request, 'index.html', context)

def digital(request):

    pictures = Picture.objects.filter(picture_type='digital')
    context = {'pictures' : pictures }

    return render(request, 'digital.html', context)

def water_color(request):

    pictures = Picture.objects.filter(picture_type='water color')
    context = {'pictures' : pictures }

    return render(request, 'water_color.html', context)

def contact(request):

    context = {}

    return render(request, 'contact.html', context)

