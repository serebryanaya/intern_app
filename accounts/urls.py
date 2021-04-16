from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('register_employer/', views.register_page_employer, name='register_employer'),
    path('register_university/', views.register_page_university, name='register_university'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('', views.index, name='home'),

    path('student_page/', views.student_page, name='student_page'),
    path('employer_page/', views.employer_page, name='employer_page'),
    path('university_page/', views.university_page, name='university_page'),

    path('update', views.update, name='update'),
    path('student_page/<int:pk>', views.StudDetailView.as_view(), name='stud_detail'),
    path('student_page/<int:pk>/update', views.StudDataUpdate.as_view(), name='stud_update'),
]