from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from account.models import Profile


def signup(request):
    if request.method == "GET":
        return render(request, 'account/signup.html')

    elif request.method == "POST":
        firstName = request.POST["first_name"]
        lastName = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 != password2:
            messages.error(request, 'Passwords are not same!')
            return redirect('signup')

        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username Already taken!')
            return redirect('signup')

        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Already have an account with this email!')
            return redirect('signup')

        else:
            user = User.objects.create_user(
                first_name=firstName, last_name=lastName, username=username, email=email, password=password1)
            Profile.objects.create(user=user)
            return redirect('login')
    else:
        return render(request, 'main/404.html')



def login(request):
    if request.method == "GET":
        return render(request, 'account/login.html')

    elif request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')

        else:
            messages.error(request, 'Invalid Credentials!')
            return redirect('login')
    else:
        return render(request, 'main/404.html')



def logout(request):
    auth.logout(request)
    return redirect('/')


