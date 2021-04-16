from django.db import models
from django.contrib.auth.models import User

#from vboard.models import Skill

# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, verbose_name='Логин')
    initials = models.CharField(max_length=200, null=True, verbose_name='ФИО')
    my_skill = models.ManyToManyField(to='vboard.Skill', blank=True, verbose_name='Навыки')
    phone = models.CharField(max_length=200, null=True, verbose_name='Телефон')
    #email = models.CharField(max_length=200, null=True, verbose_name='Почта')
    num_cert = models.CharField(max_length=200, null=True, verbose_name='Студ билет')
    about = models.TextField(null=True, verbose_name='О себе')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/student_page/{self.id}'

    class Meta:
        verbose_name_plural = 'Студенты'
        verbose_name = 'Студент'
        ordering = ['-name']


class Employer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    name_org = models.CharField(max_length=200, null=True, verbose_name='Название Организации')
    address = models.CharField(max_length=200, null=True, verbose_name='Адрес')
    #email = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True, verbose_name='Телефон')
    initials = models.CharField(max_length=200, null=True, verbose_name='ФИО')
    about = models.TextField(null=True, verbose_name='О себе')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Работодатели'
        verbose_name = 'Работодатель'
        ordering = ['-name']


class University(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, verbose_name='ФИО')
    #email = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True, verbose_name='Телефон')
    about = models.TextField(null=True, verbose_name='О себе')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Университет'
        verbose_name = 'Сотрудник университета'
        ordering = ['-name']