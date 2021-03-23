from django.shortcuts import redirect, render
from .forms import EmployeeForm
from .models import Employee

# Create your views here.


def employee_list(request):
    employees = Employee.objects.all()
    template_name = 'employees/employee_list.html'
    context = {
        'employees': employees
    }
    return render(request, template_name, context)


def employee_form(request):
    template_name = 'employees/employee_form.html'
    # For Get Request
    if request.method == "GET":
        form = EmployeeForm()
        context = {
            'form': form
        }
        return render(request, template_name, context)
    else:
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('employee_list')


def employee_update(request, id):
    template_name = 'employees/employee_form.html'
    if request.method == "GET":
        employee = Employee.objects.get(pk=id)
        form = EmployeeForm(instance=employee)
        context = {
            'form': form
        }
        return render(request, template_name, context)
    else:
        employee = Employee.objects.get(pk=id)
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
        return redirect('employee_list')


def employee_delete(request, id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('employee_list')


def employee_detail(request, id):
    employee = Employee.objects.get(pk=id)
    context = {
        'employee': employee
    }
    return render(request, 'employees/employee_detail.html', context)
