from django.urls import path
from .views import EmployeeTodayTasks

app_name = 'api'

urlpatterns = [
    path('api/today_tasks', EmployeeTodayTasks.as_view(), name='today_tasks'),
]
