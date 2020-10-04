from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from main.models import *


def index(request):

    all_post = Post.objects.all()
    restaurant = Restaurant.objects.all()


    context = {
        'posts' : all_post,
        'retaurant' : restaurant
    }
    return render(request, 'main/index.html', context)


def not_found(request):
    return render(request, 'main/404.html')

def about(request):
    return render(request, 'main/about.html')

def tour(request):
    return render(request, 'main/tours.html')

def contact(request):
    return render(request, 'main/contact.html')