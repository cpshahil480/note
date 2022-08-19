from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from note.models import Post



class PostForm(ModelForm):
    class Meta:
        model=Post
        fields='__all__'

        widgets={
            "title":forms.TextInput(attrs={"class":"form-control" }),
            "title_tag": forms.TextInput(attrs={"class": "form-control"}),
            "body": forms.TextInput(attrs={"class": "form-control"}),
        }






