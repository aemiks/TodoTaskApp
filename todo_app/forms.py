from django import forms
from django.conf import settings


TASK_CATEGORY = (
    ('EX1', 'Example Category 1'),
    ('EX2', 'Example Category 2'),
    ('EX3', 'Example Category 3'),
    ('EX4', 'Example Category 4'),
)


class EmployeeForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    hired_date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS,
                                 widget=forms.DateInput(
                                     attrs={
                                         'class': 'form-control',
                                         'type': 'date',
                                     }))
    address = forms.CharField(required=False,
                              widget=forms.TextInput(attrs={
                                  'class': 'form-control',
                              }))
    city = forms.CharField(required=False,
                           widget=forms.TextInput(attrs={
                               'class': 'form-control',
                           }))


class TaskForm(forms.Form):
    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 4
    }))
    category = forms.ChoiceField(
        choices=TASK_CATEGORY, widget=forms.Select(
            attrs={
                'class': 'form-control',
            }))
    target_date = forms.DateField(
        input_formats=settings.DATE_INPUT_FORMATS,
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date',
        }))
