# Django Web Development Projects

This repository contains a collection of web development projects built with the **Django framework**. The goal of this repository is to explore different aspects of backend development, web application architecture, and best practices when building scalable applications with Django.

Each project follows the standard Django structure and demonstrates core concepts of modern web development using Python.

---

## Project Scope

The main concepts explored across the projects in this repository include:

- Django project and app structure  
- URL routing and request handling  
- Database design using Django ORM  
- Database migrations and schema management  
- Template rendering and server-side views  
- Form handling and validation  
- Static and media file management  
- Django Admin configuration and customization  
- Basic authentication and user functionality  
- Local development and project organization  

---

## Repository Structure

This repository contains multiple Django projects, each following the standard Django layout:

```
project_name/
│
├── project_name/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── app_name/
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   ├── urls.py
│   └── migrations/
│
├── manage.py
└── db.sqlite3
```

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
```

### 2. Create a Virtual Environment (recommended)

```bash
python -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Run the Development Server

```bash
python manage.py runserver
```

Your application will be available at:

```
http://127.0.0.1:8000/
```

---

## Technologies Used

- Python  
- Django  
- SQLite (default development database)  
- HTML Templates or REST API responses  
- Django’s development utilities  

---

## Future Work

More Django projects, features, and educational samples will be added over time to expand backend development coverage.

---

## Author

Sarah M. Afshar
```
