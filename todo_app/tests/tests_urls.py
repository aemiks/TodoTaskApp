from django.test import TestCase, Client
from todo_app.models import Employee
from django.urls import reverse, resolve
from todo_app.views import home_view

client = Client()

class UrlsTestCase(TestCase):
    def setUp(self):
        #create Employee
        Employee.objects.create(
            first_name = "Piotr",
            last_name = "Nowak",
            hired_date = "2022-05-03",
            address = "Warszawska 1",
            city = "Poznan",
        )

    def test_employee_detail(self):
        employee = Employee.objects.get(first_name="Piotr")
        response = self.client.get('/employee/{}'.format(employee.id))
        self.assertEqual(response.status_code, 200)

    def test_home_status_code(self):
        url = reverse('todo_app:home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEqual(view.func, home_view)
