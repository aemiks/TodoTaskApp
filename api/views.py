from todo_app.models import Employee
from rest_framework import generics
from .serializers import EmployeeTodayTasksSerializer


class EmployeeTodayTasks(generics.ListAPIView):
    """list of all employee and tasks with today date
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeTodayTasksSerializer
