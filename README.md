# Task Management — REST API

A REST API for managing tasks with user authentication, JWT tokens, task status management, and admin access.

## What it does

Users can:

* Register and verify their account
* Login using username, email, or phone number
* Create, update and delete tasks
* Change task status
* Search tasks by status
* View only their own tasks

Admins can:

* View all users' tasks
* See task owners, statuses, created and updated times

## Tech Stack

* Python, Django, Django REST Framework
* PostgreSQL
* JWT Authentication
* Postman for testing

## Project Structure

```text
task_management/
├── config/          # settings, root urls
├── users/           # authentication and user management
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
├── tasks/           # task management
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
├── shared/          # shared models and utilities
├── manage.py
├── Pipfile
└── requirement.txt
```

## Models

| Model  | Fields                                                                    | Description       |
| ------ | ------------------------------------------------------------------------- | ----------------- |
| `User` | `username`, `email`, `phone_number`, `auth_status`                        | Application users |
| `Task` | `title`, `description`, `task_status`, `user`, `created_at`, `updated_at` | User tasks        |

### Task Status

* `newly_added`
* `pending`
* `finished`

## Setup

```bash
git clone https://github.com/khasanmukhammad/task_management.git
cd task_management

pipenv install
pipenv shell
```

Create a `.env` file with your database and application settings.

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## API

### Users

```text
POST /users/signup/
POST /users/login/
POST /users/login/refresh/
POST /users/logout/
POST /users/verify/
POST /users/new-verify/
PATCH /users/change-user/
POST /users/forget-password/
POST /users/reset-password/
```

### Tasks

```text
GET    /tasks/tasks/
POST   /tasks/create/
GET    /tasks/<uuid:pk>/
PATCH  /tasks/<uuid:pk>/
DELETE /tasks/<uuid:pk>/
PATCH  /tasks/<uuid:pk>/change-status/
POST   /tasks/task-status/
GET    /tasks/admin/ #permission only admin
```

## Authentication

Protected endpoints require a JWT access token.

```text
Authorization: Bearer <access_token>
```

## Example

### Create Task

```json
{
    "title": "Learn Django",
    "description": "Study Django REST Framework"
}
```

New tasks are created with:

```text
task_status: newly_added
```

### Change Status

```json
{
    "task_status": "pending"
}
```

## Admin

Create an admin:

```bash
python manage.py createsuperuser
```

Admin can access all users' tasks through:

```text
GET /tasks/admin/
```

## Note

`.env` and database files should not be committed to Git.
