from django.db import models

#from accounts.models import Employer

# Create your models here.
class Vacancy(models.Model):
    title = models.CharField(max_length=50, verbose_name='Вакансия')
    owner = models.ForeignKey(to='accounts.Employer', on_delete=models.PROTECT, verbose_name='Работодатель')
    skills = models.ManyToManyField('Skill', blank=True, verbose_name='Навыки')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Стажировки'
        verbose_name = 'Стажировка'
        ordering = ['-published']

class Skill(models.Model):
    OWNER = [
        ('U', 'university'),
        ('E', 'employer'),
    ]

    name = models.CharField(max_length=50, db_index=True, verbose_name='Навык')
    owner = models.CharField(max_length=1, choices=OWNER, default='E', verbose_name='Создатель')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Навыки'
        verbose_name = 'Навык'
        ordering = ['name']