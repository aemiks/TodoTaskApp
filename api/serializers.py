from todo_app.models import Task, Employee
from rest_framework import serializers
from datetime import date


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['description', 'is_active',
                  'category', 'create_date', 'target_date']


class EmployeeTodayTasksSerializer(serializers.ModelSerializer):
    tasks = serializers.SerializerMethodField()

    def get_tasks(self, employee):
        """Filter Tasks qs to serializer, only tasks with today target_date
            and only active tasks
        """
        qs = Task.objects.filter(target_date=date.today(), is_active=True, employee=employee)
        serializer = TaskSerializer(instance=qs, many=True)
        return serializer.data

    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name',
                  'hired_date', 'address', 'city', 'tasks']
