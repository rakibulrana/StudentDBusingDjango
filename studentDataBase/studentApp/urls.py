from django.urls import path
from studentApp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('insert', views.insertStudentData, name='insertStudentData'),
    path('update/<id>', views.updateData, name='updateData'),  # url path for the href action of the edit button

    path('delete/<id>', views.delete, name="Delete"),  # url path for the href action of the delete button

]
