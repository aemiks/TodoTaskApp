from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Employee, Task
from .forms import EmployeeForm, TaskForm
from django.http import JsonResponse
from .filters import TaskFilter
from django.contrib import messages
import csv
from django.template.loader import render_to_string


def home_view(request):
    """Simple home view, to list all Employee model and add new one
        with validation:
          - it is not possible to add an employee with
            the same name and lastname, hired on the same day
    """
    context = {}
    employees = Employee.objects.all()
    form = EmployeeForm(request.POST)

    if form.is_valid():
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        address = form.cleaned_data['address'] or "N/A"
        city = form.cleaned_data['city'] or "N/A"
        hired_date = form.cleaned_data['hired_date']

        # validation to check if Employee isnt already in database
        qs = Employee.objects.filter(
            first_name=first_name, last_name=last_name, hired_date=hired_date)
        if qs.exists():
            messages.error(
                request, "This Employee is already at Employees List",
                extra_tags='alert alert-danger')
            return redirect('/')

        # add new employee if not already in database
        else:
            new_employee = Employee(
                first_name=first_name,
                last_name=last_name,
                address=address,
                city=city,
                hired_date=hired_date,
            )
            new_employee.save()
            messages.success(request, "New Employee added.",
                             extra_tags='alert alert-success')

    context['employees'] = employees
    context['form'] = form

    return render(request, 'home.html', context)


def employee_detail(request, id):
    """Render Employee details with all tasks assigned to
    """
    context = {}
    form = TaskForm(request.POST or None)
    try:
        employee = Employee.objects.get(id=id)
        tasks = Task.objects.filter(employee=employee)

        # filter parameter available: is_active and target_date
        filter = TaskFilter(request.GET, queryset=tasks)

        context['employee'] = employee
        context['tasks'] = tasks
        context['form'] = form
        context['filter'] = filter

        if form.is_valid():
            description = form.cleaned_data['description']
            category = form.cleaned_data['category']
            target_date = form.cleaned_data['target_date']

            # add new task
            new_task = Task(
                employee=employee,
                description=description,
                category=category,
                target_date=target_date,
                is_active=True,
            )
            new_task.save()
            messages.success(request, "New task added.",
                             extra_tags='alert alert-success')
            return redirect("todo_app:employee_detail", id=employee.id)
    except:
        messages.error(request, "Something wrong, employee does not exists.",
                       extra_tags='alert alert-success')
        return redirect("todo_app:employee_detail", id=employee.id)
    return render(request, 'todo_app/employee_detail.html', context)


def delete_task(request):
    """Function to permanently delete selected task by ajax
    """
    id = request.GET.get('id')
    task = get_object_or_404(Task, id=id)
    employee = task.employee
    task.delete()

    tasks = Task.objects.filter(employee=employee)
    filter = TaskFilter(request.GET, queryset=tasks)

    html = render_to_string(
        'section.html', {'filter': filter, 'employee': employee})
    return JsonResponse(html, safe=False)


def finish_task(request):
    """Function to set is_active Task to "False" by ajax
    """
    id = request.GET.get('id')
    task = get_object_or_404(Task, id=id)
    task.is_active = False
    employee = task.employee
    task.save()

    tasks = Task.objects.filter(employee=employee)
    filter = TaskFilter(request.GET, queryset=tasks)

    html = render_to_string(
        'section.html', {'filter': filter, 'employee': employee})
    return JsonResponse(html, safe=False)


def reopen_task(request):
    """Function to set is_active Task to "True" by ajax
    """
    id = request.GET.get('id')
    task = get_object_or_404(Task, id=id)
    task.is_active = True
    employee = task.employee
    task.save()

    tasks = Task.objects.filter(employee=employee)
    filter = TaskFilter(request.GET, queryset=tasks)

    html = render_to_string(
        'section.html', {'filter': filter, 'employee': employee})
    return JsonResponse(html, safe=False)


def export_tasks_csv(request, id):
    """Function uses "csv" library to retrive
        selected Employee tasks and add to .csv file
    """
    respone = HttpResponse(content_type='text/csv')
    respone['Content-Disposition'] = 'attachment; filename="employee_tasks.csv"'
    writer = csv.writer(respone)

    # create first line with data table names
    writer.writerow(['employee_id', 'employee_first_name', 'employee_last_name',
                    'description', 'is_active', 'category', 'target_date'])

    # loop through all tasks and add each one to separate line
    employee = Employee.objects.get(id=id)
    tasks = Task.objects.filter(employee=employee).values_list(
        'employee_id', 'employee__first_name', 'employee__last_name',
        'description', 'is_active', 'category', 'target_date')
    for task in tasks:
        writer.writerow(task)

    return respone
