from django.shortcuts import render
from .models import StudentDataBase


def insertStudentData(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST['age']
        gender = request.POST['gender']

        print(name, email, age, gender)

        query = StudentDataBase(name=name, email=email, age=age, gender=gender)
        query.save()

    return render(request, 'index.html')


def index(request):
    # get the data from DB and show that in font-end
    student_data = StudentDataBase.objects.all()  # Retrieve all student records from the database

    context = {'student_data': student_data}  # Create a context dictionary and add the students data

    return render(request, 'index.html', context)  # Render the template with the context data
