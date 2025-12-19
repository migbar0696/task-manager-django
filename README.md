# Task Management API README

# **Task Management API** (BE Capstone Project)

## **Project Overview**

The Task Management API is a backend application built with **Django** and **Django REST Framework (DRF)**. It allows users to manage their daily tasks by creating, updating, deleting, and marking tasks as complete or incomplete. The API ensures each user can only access their own tasks, simulating real-world backend development with secure authentication, database management, and RESTful API design.

**Originality Enhancements:**
To make this project unique and go beyond the standard requirements, we added the following features:

1. **Task Categories** – Users can create categories (e.g., Work, Personal) and assign tasks to them.
2. **Recurring Tasks** – Users can create recurring tasks (Daily/Weekly/Monthly) that regenerate automatically after completion.
3. **Priority Sorting & Status Filtering** – Tasks can be filtered and sorted by priority, due date, status, and category.
4. **Task History Log** – Keep a record of completed tasks for reference.
5. **Task Collaboration** – Users can share a task with other users, giving them permission to view or edit it.

---

## **Functional Requirements**

### **Tasks**

* **CRUD operations:** Create, Read, Update, Delete tasks
* **Attributes:**

  * `title` (string)
  * `description` (string)
  * `due_date` (datetime)
  * `priority` (Low, Medium, High)
  * `status` (Pending, Completed)
  * `category` (optional, e.g., Work, Personal)
  * `recurring` (optional, Daily/Weekly/Monthly)
  * `completed_at` (datetime, automatically set when marked complete)
* **Mark as Complete/Incomplete:** Custom endpoint to toggle task status
* **Filters & Sorting:** Filter by status, priority, due_date, category; sort by priority or due_date
* **Ownership & Permissions:** Users can only access and edit their own tasks; shared tasks can be edited by collaborators

### **Users**

* **CRUD operations:** Register, Read profile, Update profile, Delete account
* **Attributes:**

  * `username` (unique)
  * `email` (unique)
  * `password` (hashed)
* **Authentication:** Token-based JWT authentication to secure endpoints

---

## **API Endpoints**

| Endpoint                    | Method    | Description                                                   |
| --------------------------- | --------- | ------------------------------------------------------------- |
| `/api/users/register/`      | POST      | Register new user                                             |
| `/api/users/login/`         | POST      | Obtain authentication token                                   |
| `/api/users/me/`            | GET       | Get current user profile                                      |
| `/api/tasks/`               | GET       | List all tasks of the logged-in user (with filters & sorting) |
| `/api/tasks/`               | POST      | Create a new task                                             |
| `/api/tasks/<id>/`          | GET       | Retrieve task details                                         |
| `/api/tasks/<id>/`          | PUT/PATCH | Update a task (cannot update completed tasks unless reverted) |
| `/api/tasks/<id>/`          | DELETE    | Delete a task                                                 |
| `/api/tasks/<id>/complete/` | POST      | Mark task as complete/incomplete                              |
| `/api/tasks/<id>/share/`    | POST      | Share task with other users (original feature)                |

---

## **Technical Requirements**

* **Framework:** Django, Django REST Framework
* **Database:** SQLite (development), Postgres (for production)
* **Authentication:** JWT (via `djangorestframework-simplejwt`)
* **Deployment:** Heroku or PythonAnywhere
* **Validations:**

  * Due date must be in the future
  * Priority must be Low, Medium, or High
  * Completed tasks cannot be edited unless reverted

---

## **Stretch Goals / Original Features**

1. **Recurring Tasks:** Automatically regenerate tasks based on recurrence.
2. **Task Categories:** Organize tasks by category.
3. **Task History Log:** Track completed tasks with timestamps.
4. **Collaborative Tasks:** Share tasks with other users.
5. **Enhanced Filtering:** Filter tasks by status, priority, due date, and category.

---

## **Getting Started**

### **Clone the Repository**

```bash
git clone <your-repo-url>
cd task_management_api
```

### **Create a Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### **Install Dependencies**

```bash
pip install -r requirements.txt
```

### **Run Migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

### **Create a Superuser**

```bash
python manage.py createsuperuser
```

### **Run the Server**

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/api/`

---

## **Deployment**

* Prepare `requirements.txt`, `Procfile`, and `runtime.txt` for Heroku
* Push to GitHub and deploy on Heroku or PythonAnywhere
* Test all endpoints after deployment

---

## **Conclusion**

This Task Management API project provides a realistic backend development experience. It is fully RESTful, secure, and scalable. With original enhancements like task collaboration, recurring tasks, and history tracking, it stands out as a professional-grade project suitable for a capstone submission.
