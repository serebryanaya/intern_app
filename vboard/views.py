from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Vacancy, Skill
from .forms import VacancyForm
from accounts.models import Employer

# Create your views here.

def vacancy_board_stud(request):
    vacancies = Vacancy.objects.all()

    context = {'vacancies': vacancies}
    return render(request, 'vboard/vacancy_board_stud.html', context)


def vacancy_board_emp(request):
    owner_id = Employer.objects.filter(user=request.user.pk).first()
    vacancies = Vacancy.objects.filter(owner=owner_id)

    context = {'vacancies': vacancies}
    return render(request, 'vboard/vacancy_board_emp.html', context)


class VacancyCreateView(CreateView):
    template_name = 'vboard/create_v.html'
    form_class = VacancyForm
    success_url = reverse_lazy('vacancy_board_emp')