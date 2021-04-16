from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView

# Create your views here.
from .forms import CreateUserForm, StudentForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from .decorators import allowed_users
from .models import Student, Employer, University

# Домашняя страница: проверка на наличие юзера в группе
def index(request):
    context = {}
    if request.user.is_authenticated:
        if request.user.groups.filter(name='student').exists():
            context = {'groups': 'student'}
        elif request.user.groups.filter(name='employer').exists():
            context = {'groups': 'employer'}
        elif request.user.groups.filter(name='university').exists():
            context = {'groups': 'university'}
    return render(request, 'home.html', context)


# Регистрация студентов, работодателей, университета
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')

                group_name = request.POST.get('staff')
                group = Group.objects.get(name=group_name)
                user.groups.add(group)
                if group_name == 'student':
                    Student.objects.create(
                        user=user,
                        name=user.username,
                    )
                elif group_name == 'employer':
                    Employer.objects.create(
                        user=user,
                        name=user.username,
                    )
                elif group_name == 'university':
                    University.objects.create(
                        user=user,
                        name=user.username,
                    )

                messages.success(request, 'Аккаунт создан для ' + username)
                return redirect('login')
        context = {'form': form}
        return render(request, 'accounts/register.html', context)

# можно удалить
# Регистрация работодателей
def register_page_employer(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')

                group = Group.objects.get(name='employer')
                user.groups.add(group)
                Employer.objects.create(
                    user=user,
                    name=user.username,
                )
                
                messages.success(request, 'Аккаунт создан для ' + username)
                return redirect('login')
        context = {'form': form}
        return render(request, 'accounts/register_employer.html', context)

# можно удалить
# Регистрация университета
def register_page_university(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')

                group = Group.objects.get(name='university')
                user.groups.add(group)
                University.objects.create(
                    user=user,
                    name=user.username,
                )
                
                messages.success(request, 'Аккаунт создан для ' + username)
                return redirect('login')
        context = {'form': form}
        return render(request, 'accounts/register_university.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Имя или пароль неверные!!')
        context = {}
        return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def student_page(request):
    student = Student.objects.filter(user=request.user)
    return render(request, 'accounts/student_page.html', {'student': student})


# Данные студента
class StudDetailView(DetailView):
    model = Student
    template_name = 'accounts/stud_detail.html'
    context_object_name = 'student'


# Обновление данных студента
class StudDataUpdate(UpdateView):
    model = Student

    template_name = 'accounts/stud_update.html'
    form_class = StudentForm


def update(request):
    error = ''
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stud_detail')
        else:
            error = 'Форма не верная'

    form = StudentForm()

    context = {
        'form': form,
        'error': error
    }

    return render(request, 'accounts/stud_update.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['employer'])
def employer_page(request):
    context = {}
    return render(request, 'accounts/employer_page.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['university'])
def university_page(request):
    context = {}
    return render(request, 'accounts/university_page.html')