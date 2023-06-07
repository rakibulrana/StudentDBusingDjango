from django.shortcuts import render


def index(request):

    return render(request, 'index.html')

def insertStudentData(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')

        print(name,email, age, gender)


    return render(request, 'index.html')