from django.urls import path
from .views import (
    home_view,
    employee_detail,
    delete_task,
    finish_task,
    reopen_task,
    export_tasks_csv,
)

app_name = 'todo_app'

urlpatterns = [
    path('', home_view, name='home'),
    path('employee/<int:id>', employee_detail, name='employee_detail'),
    path('export/<int:id>', export_tasks_csv, name='export_tasks_csv'),

    path('ajax/delete_task/', delete_task, name='delete_task'),
    path('ajax/finish_task/', finish_task, name='finish_task'),
    path('ajax/reopen_task/', reopen_task, name='reopen_task'),
]
