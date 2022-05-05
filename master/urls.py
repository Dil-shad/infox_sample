from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('add_course', add_course, name='add_course'),
    path('student_fun',student_fun,name='student_fun'),
    path('',show_std,name='show_std'),

]
