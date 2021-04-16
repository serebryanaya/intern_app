from django.contrib import admin
from .models import Vacancy, Skill

# Register your models here.
admin.site.register(Vacancy)
admin.site.register(Skill)

class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner')

class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner')