from django.http.response import JsonResponse
from django.shortcuts import render
from .forms import StudentRegistrationForm
from .models import Student

# Create your views here.


def index(request):
    form = StudentRegistrationForm
    students = Student.objects.all()
    context = {
        'form': form,
        'students': students
    }
    return render(request, 'ajax_2/index.html', context)


def save_data(request):
    if request.method == "POST":
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            student = Student(name=name, email=email, password=password)
            student.save()
            students = Student.objects.values()
            students_list = list(students)
            return JsonResponse({'status': 'Success', 'students_list': students_list})
        return JsonResponse({'status': 'Error'})
