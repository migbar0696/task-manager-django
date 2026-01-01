# Task Management API

This README documents the features that are implemented in this repository as of now.

**Overview**

This backend API is built with Django and Django REST Framework. It provides authenticated task management for users: creating, reading, updating, deleting, and marking tasks completed or incomplete. Authentication uses JWT tokens.

**Implemented Features**

- **Tasks — CRUD:** Create, retrieve, update, and delete tasks via the `TaskViewSet` at `/api/tasks/`.
- **Task attributes:** `title`, `description`, `due_date`, `priority` (Low/Medium/High), `status` (Pending/Completed), `recurring` (field present), `completed_at`, `owner`, and optional `category` (model present).
- **Ownership:** Tasks are owned by a user; users only see their own tasks. New tasks are saved with the requesting user as `owner`.
- **Mark complete/incomplete:** Custom actions `mark_complete` and `mark_incomplete` exist on the task viewset to mark tasks completed or pending.
- **Filters & ordering:** Basic filtering by `status`, `priority`, and `category__name` and ordering by `due_date` and `priority` are enabled.
- **Validations:** `due_date` is validated to be in the future in the task serializer.
- **Authentication:** JWT authentication configured. Token endpoints are available at `/api/token/` and `/api/token/refresh/`.

**API Endpoints (implemented)**

- `POST /api/token/` — Obtain JWT access and refresh tokens.
- `POST /api/token/refresh/` — Refresh JWT access token.
- `GET /api/tasks/` — List tasks for the authenticated user (supports filtering and ordering).
- `POST /api/tasks/` — Create a new task (owner set to authenticated user).
- `GET /api/tasks/{id}/` — Retrieve a specific task (must be owner).
- `PUT/PATCH /api/tasks/{id}/` — Update a task (no special block on completed tasks currently).
- `DELETE /api/tasks/{id}/` — Delete a task.
- `POST /api/tasks/{id}/mark_complete/` — Mark task as completed (sets `completed_at`).
- `POST /api/tasks/{id}/mark_incomplete/` — Mark task as pending (clears `completed_at`).

**Notable implementation details**

- `Category` model exists and is linked to `Task`, but there are no dedicated category API endpoints implemented yet.
- The `recurring` field exists on `Task`, but automatic regeneration logic is not implemented here.

**Getting started (development)**

```bash
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

The API base path is `http://127.0.0.1:8000/api/`.

**Notes**

- JWT token endpoints are in the project URLs (`/api/token/` and `/api/token/refresh/`).
- Authorization is required for all task endpoints; include the `Authorization: Bearer <access_token>` header.

---

This README reflects only the features implemented in the codebase now.
