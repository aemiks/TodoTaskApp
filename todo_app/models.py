from django.db import models
import datetime


TASK_CATEGORY = (
    ('EX1', 'Example Category 1'),
    ('EX2', 'Example Category 2'),
    ('EX3', 'Example Category 3'),
    ('EX4', 'Example Category 4'),
)


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    hired_date = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return str(self.first_name + ' ' + self.last_name)

    def active_tasks_count(self):
        count = 0
        for task in Task.objects.filter(employee=self):
            if task.is_active:
                count += 1
        return count

    def finished_tasks_count(self):
        count = 0
        for task in Task.objects.filter(employee=self):
            if not task.is_active:
                count += 1
        return count


class Task(models.Model):
    employee = models.ForeignKey(
        Employee, related_name='tasks',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    description = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    category = models.CharField(choices=TASK_CATEGORY, max_length=3)
    create_date = models.DateTimeField(auto_now_add=True)
    target_date = models.DateField()

    def __str__(self):
        return self.description

    def timeleft_to_target(self):
        if self.target_date:
            return self.target_date - datetime.datetime.now().date()
        else:
            return None
