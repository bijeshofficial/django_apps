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
            sid = request.POST.get('sid')
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']

            if sid == "":
                student = Student(name=name, email=email, password=password)
            else:
                student = Student(id=sid, name=name,
                                  email=email, password=password)
            student.save()
            students = Student.objects.values()
            students_list = list(students)
            return JsonResponse({'status': 'Success', 'students_list': students_list})
        return JsonResponse({'status': 'Error'})


def delete_data(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        student = Student.objects.get(pk=id)
        student.delete()
        return JsonResponse({'status': 1})
    return JsonResponse({'status': 0})


def update_data(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        student = Student.objects.get(pk=id)
        student_data = {"id": student.id, "name": student.name,
                        "email": student.email, "password": student.password}
        return JsonResponse(student_data)
