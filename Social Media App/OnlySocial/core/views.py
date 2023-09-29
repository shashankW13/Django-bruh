from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Profile
from django.contrib.auth.decorators import login_required

@login_required(login_url='core:signin')
def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('core:signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('core:signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('core:signup')
            else:
                user = User.objects.create_user(username=username,
                                                email=email,
                                                password=password)
                user.save()

                #log user in and direct to settings page

                #create a profile object for the new user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('core:singin')
        else:
            messages.info(request, 'Passwords not matching')
            return redirect('core:signup')

    else:
        return render(request, 'signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Incorrect credentials')
            return redirect('core:signin')
    else:
        return render(request, 'signin.html')

@login_required(login_url='core:signin')
def logout(request):
    auth.logout(request)
    return redirect('core:signin')
