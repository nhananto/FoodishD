from django.shortcuts import render



def index(request):
    return render(request, 'main/index.html')


def not_found(request):
    return render(request, 'main/404.html')
