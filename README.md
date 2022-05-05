
## ToDoTaskApp - Assigment Task

 _ToDoTaskApp assigment Task_ - web online version: https://assigment-todoapp.herokuapp.com/


## Table of contents
* [Swagger](#swagger)
* [Technologies](#technologies)
* [Setup](#setup)
* [Tests](#tests)

## Swagger

Check API docs on Swagger here: https://aemiks.github.io/TodoTaskApp/


## Endpoint list  

    / - home view with all employees list
    emoloyee/<id> - employee details with all tasks
    api/today_tasks/ - API (check Swagger-docs)


## Technologies
Project is created with:
* ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django)
* ![](https://img.shields.io/badge/django%20version-4.0.0-blue)


## Setup

Please download the appropriate environment and read the instructions for installing it
* [Python](https://www.python.org/downloads/)
* [Django](https://docs.djangoproject.com/en/3.2/topics/install/)


### Build

```sh
$ git clone https://github.com/aemiks/TodoTaskApp.git
$ cd todotaskapp
$ docker-compose up --build
```

### Update tables in a database

`python manage.py migrate`

### Run development server

`python manage.py runserver`

## Tests

To run the tests type:

`python manage.py test `
