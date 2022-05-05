from django.test import TestCase
from todo_app.models import Employee, Task


class EmployeeTestCase(TestCase):
    def setUp(self):
        #create Employee
        Employee.objects.create(
            first_name = "Piotr",
            last_name = "Nowak",
            hired_date = "2022-05-03",
            address = "Warszawska 1",
            city = "Poznan",
        )
        employee = Employee.objects.get(id=1)

        #create active task
        Task.objects.create(
            employee = employee,
            description = "Test Active Task description",
            is_active = True,
            category = "EX1",
            create_date = "2022-05-03",
            target_date = "2022-05-05",
        )

        # create not active task
        Task.objects.create(
            employee = employee,
            description = "Test Active Task description",
            is_active = False,
            category = "EX1",
            create_date = "2022-05-03",
            target_date = "2022-05-05",
        )

    def test_active_tasks_count(self):
        employee = Employee.objects.get(id=1)
        self.assertEqual(employee.active_tasks_count(), 1)

    def test_finished_tasks_count(self):
        employee = Employee.objects.get(id=1)
        self.assertEqual(employee.finished_tasks_count(), 1)
