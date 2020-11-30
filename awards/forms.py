from django import forms
from django.contrib.auth.models import User
from .models import Profile, Project
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']

    def save(self, commit=True):
        user=super().save(commit=False)
        user.email=self.cleaned_data['email']
        if commit:
            user.save()
        return user

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['prof_pic', 'bio']
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['prof_pic', 'bio']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProjectForm(forms.ModelForm):
    class Meta:
        model=Project
        fields=['title', 'image', 'description', 'url']