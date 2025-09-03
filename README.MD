

#  Healthcare Backend API (Django + DRF + PostgreSQL + JWT)

A backend service for managing **patients, doctors, and their mappings**.  
Built with **Django 5, Django REST Framework, PostgreSQL, and JWT authentication**.

---

## Features

-  User registration & JWT-based login
-  CRUD for Doctors
- CRUD for Patients (per-user ownership)
- Assign patients to doctors (with uniqueness validation)
- Token-based authentication (access & refresh tokens)
-  Clean RESTful API with DRF viewsets & routers

---

## Tech Stack

- **Python 3.10+**
- **Django 5+**
- **Django REST Framework**
- **djangorestframework-simplejwt**
- **PostgreSQL**
- **django-environ**

---

##  Setup Instructions

### 1. Clone repo & create virtual environment
```bash
git clone <https://github.com/Palakmalik1594/Healthcare-whatbytes.git>
cd healthcare
python -m venv venv
# Activate
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

2. Install dependencies

pip install -r requirements.txt

3. Configure environment

Create a .env file in the project root (healthcare/.env):

DEBUG=True
SECRET_KEY=replace-with-strong-secret-key

# Database
DB_NAME=healthcare_db
DB_USER=postgres
DB_PASSWORD=postgres  #whatever your password is 
DB_HOST=127.0.0.1
DB_PORT=5432

# JWT settings
ACCESS_TOKEN_LIFETIME_MINUTES=60
REFRESH_TOKEN_LIFETIME_DAYS=7
ALLOWED_HOSTS=*

4. Setup PostgreSQL

CREATE DATABASE healthcare_db;
CREATE USER postgres WITH PASSWORD 'postgres';
GRANT ALL PRIVILEGES ON DATABASE healthcare_db TO postgres;

5. Run migrations & start server

python manage.py makemigrations
python manage.py migrate
python manage.py runserver

#first visit 
http://http://127.0.0.1:8000/

API will be available at:
   
👉 http://127.0.0.1:8000/api/


#for viewing all data and enteries:
  http://127.0.0.1:8000/admin/

#
---
