from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile, Project
from django.http import HttpRequest, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import RegistrationForm, ProfileForm, UserUpdateForm, ProjectForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from itertools import chain
from django.urls import reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

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
        'posts':Project.objects.all(),
    }

    return render(request, 'index.html', context)

@login_required
def searchprofile(request): 
    if 'searchUser' in request.GET and request.GET['searchUser']:
        name = request.GET.get("searchUser")
        searchResults = Profile.search_profile(name)
        message = f'name'
        params = {
            'results': searchResults,
            'message': message
        }
        return render(request, 'main/search.html', params)
    else:
        message = "You haven't searched"
    return render(request, 'main/search.html', {'message': message})

def like_image(request, pk):
    post= get_object_or_404(Project, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('gram-landing', args=[str(pk)]))


def PostCreateView(request):
    if request.method=='POST':
        form=ProjectForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, f'You have successfuly posted your project for review!')
        return redirect('gram-landing')
    else:
        form = ProfileForm()    

    return render(request, 'posts/postForm.html', {"form":form})



# class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#     model = Project
#     success_url = '/'
#     template_name= 'posts/delete.html'

#     def test_func(self):
#         post = self.get_object()
#         if self.request.user.profile == post.author:
#             return True
#         return False
