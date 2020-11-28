from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile
from django.http import HttpRequest, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import RegistrationForm, ProfileForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from itertools import chain
from django.urls import reverse

# Create your views here.
def register(request):
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        profForm=ProfileForm(request.POST, request.FILES)
        if form.is_valid() and profForm.is_valid():
            username=form.cleaned_data.get('username')
            user=form.save()
            profile=profForm.save(commit=False)
            profile.user=user
            profile.save()

            messages.success(request, f'Successfully created Account!.You can now login as {username}!')
        return redirect('login')
    else:
        form= RegistrationForm()
        profForm=ProfileForm()
    context={
        'form':form,
        'profForm': profForm
    }
    return render(request, 'users/register.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        useForm=UserUpdateForm(request.POST, instance=request.user)
        profForm=ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if useForm.is_valid() and profForm.is_valid():
            useForm.save()
            profForm.save()
            messages.success(request, f'Your account has been updated!')
        return redirect('profile')
    
    else:
        useForm=UserUpdateForm(instance=request.user.profile)
        profForm=ProfileUpdateForm(instance=request.user.profile)

    context={
        'useForm':useForm,
        'profForm':profForm
    }

    return render(request, 'users/profile.html', context)

def index(request):
    context={
        'posts':Post.objects.all(),
    }

    return render(request, 'index.html', context)
