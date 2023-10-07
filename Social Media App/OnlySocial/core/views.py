from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Profile, Post, LikePost
from django.contrib.auth.decorators import login_required

@login_required(login_url='core:signin')
def index(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)

    posts = Post.objects.all()
    return render(request, 'index.html', {'user_profile': user_profile,
                                          'posts': posts})

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
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)

                #create a profile object for the new user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('core:settings')
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

@login_required(login_url='core:signin')
def settings(request):
    user_profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        image = request.FILES.get('image')
        bio = request.POST['bio']
        location = request.POST['location']
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        email = request.POST['email']
        work = request.POST['work']
        relationship = request.POST['relationship']

        if image:
            user_profile.profile_img = image

        user_profile.bio = bio
        user_profile.location = location
        user_profile.first_name = first_name
        user_profile.last_name = last_name
        user_profile.email = email
        user_profile.work = work
        user_profile.relationship = relationship
        user_profile.save()

    return render(request, 'setting.html', {'user_profile': user_profile})

@login_required(login_url='signin')
def upload(request):
    if request.method == 'POST':
        user = request.user.username
        image_uploaded = request.FILES.get('image_upload')
        caption = request.POST['caption']

        new_post = Post.objects.create(user=user,
                                       image=image_uploaded,
                                       caption=caption)
        new_post.save()

        return redirect('/')
    else:
        return redirect('/')

@login_required(login_url='signin')
def like_post(request, post_id):
    username = request.user.username
    # post_id = request.GET.get('post_id')
    post = Post.objects.get(id=post_id)
    like_filter = LikePost.objects.filter(post_id=post_id, username=username).first()

    if like_filter is None:
        new_like = LikePost.objects.create(post_id=post_id, username=username)
        new_like.save()
        post.number_of_likes += 1
        post.save()
        return redirect('/')
    else:
        like_filter.delete()
        post.number_of_likes -= 1
        post.save()
        return redirect('/')