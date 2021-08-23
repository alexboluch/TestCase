from django import forms
from django.forms import ModelForm
from .models import GitUser, Repository


class GitUserForm(ModelForm):
    class Meta:
        model = GitUser
        fields = ("username", )
