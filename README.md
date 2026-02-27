# 📝 Django CBV Todo App

A full-featured Todo application built with Django using Class-Based Views (CBV), authentication system, and production deployment on Render.

---

## 🌐 Live Demo

👉 https://django-cbv-todo.onrender.com

---

## 🔑 Demo Admin Access

You can access the admin panel here:

👉 https://django-cbv-todo.onrender.com/admin

**Username:** demo_admin  
**Password:** Demo12345!

> Note: This is a demo project for portfolio purposes.

---

## ✨ Features

- User Authentication (Register / Login / Logout)
- Task CRUD (Create, Update, Delete)
- Mark tasks as completed
- Class-Based Views (CBV)
- Production-ready configuration
- Environment variables support
- Automatic superuser creation on deploy
- Deployed on Render

---

## 🛠 Tech Stack

- Python
- Django
- SQLite (for demo deployment)
- Gunicorn
- Render (Cloud Hosting)

---

## 🚀 Installation (Local Setup)

```bash
git clone https://github.com/your-username/Django-CBV-Todo.git
cd Django-CBV-Todo
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver