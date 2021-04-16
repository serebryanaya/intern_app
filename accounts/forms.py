from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, Textarea, CheckboxSelectMultiple
from django import forms

from .models import Student


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['initials', 'my_skill', 'phone', 'about']

        widgets = {
            "initials": TextInput(attrs={
                'placeholder': 'ФИО',
            }),
            "my_skill": CheckboxSelectMultiple(),
            "phone": TextInput(attrs={
                'placeholder': 'Телефон',
            }),
            "about": Textarea(attrs={
                'placeholder': 'О себе',
            })
        }