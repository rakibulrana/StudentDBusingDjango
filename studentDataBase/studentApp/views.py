from django.shortcuts import render, redirect
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


def updateData(request, id):
    # we will take the index function conditions to perform our tasks.
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        age = request.POST['age']
        gender = request.POST['gender']

        edit = StudentDataBase.objects.get(id=id)  # we will filter the particular data with the id, so get id!
        edit.name = name  # whatever we done in the edit part has to to follow and save there
        edit.email = email
        edit.age = age
        edit.gender = gender
        edit.save()  # save the entire edit thing

        return redirect("/")  # and redirect to the home!

    d = StudentDataBase.objects.get(
        id=id)  # to filer the particular data the query would be the line and filtered by id!
    context = {'d': d}  # we must have to change the student dictionary and its variable names
    return render(request, 'update.html', context)  # refer to newly created edit.html page


def deleteData(request, id):
    # filtered the request by ID
    d = StudentDataBase.objects.get(id=id)
    d.delete()      #delete
    return redirect("/")    #redirect the homepage
