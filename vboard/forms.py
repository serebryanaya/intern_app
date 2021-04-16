from django.forms import ModelForm
from django import forms

from .models import Vacancy, Skill

class VacancyForm(ModelForm):
    skills = forms.ModelMultipleChoiceField(queryset=Skill.objects.all(), widget=forms.CheckboxSelectMultiple())
    class Meta:
        model = Vacancy
        fields = ('title', 'owner', 'content', 'skills')