from django.urls import path
from . import views

urlpatterns = [
    path('vacancy_board/', views.vacancy_board_emp, name='vacancy_board_emp'),
    path('internship_board/', views.vacancy_board_stud, name='vacancy_board_stud'),
    path('create_vacancy/', views.VacancyCreateView.as_view(), name='create_v'),
]