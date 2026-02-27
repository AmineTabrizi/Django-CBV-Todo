# Django CBV Todo App

A clean and structured Todo application built with Django using Class-Based Views (CBV).  
This project demonstrates best practices for Django project structure, reusable apps, and modern development workflow.

---

## 🚀 Features

- Create, Update, Delete Todos
- Class-Based Views (ListView, CreateView, UpdateView, DeleteView)
- Django Forms
- Clean project structure
- Ready for production configuration
- Git & environment separation

---

## 🛠 Tech Stack

- Python 3.x
- Django 4.x / 5.x
- SQLite (default)
- Class-Based Views

## ⚙️ Installation

bash
# 1️⃣ Clone the repository
git clone https://github.com/AmineTabrizi/django-cbv-todo.git
cd django-cbv-todo

# 2️⃣ Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Apply migrations & run server
python manage.py migrate
python manage.py runserver


Open your browser and go to:
http://127.0.0.1:8000
