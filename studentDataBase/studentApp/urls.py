from django.urls import path
from studentApp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('insert', views.insertStudentData, name='insertStudentData'),
]
