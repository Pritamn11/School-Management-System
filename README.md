# School Management System
#### The School Management System is a web application designed to streamline the registration and login processes for students and teachers. Built with Django Rest Framework, this application features a PostgreSQL database hosted on Railway.app .

## How to run?

### STEPS: 

Clone the repository 

```bash
git clone https://github.com/Pritamn11/School-Management-System.git
```

#### STEPS 01 - Create a virtual environment after opening the repository

```bash
python -m venv newenv
```

```bash
.\newenv\Scripts\activate
```

#### STEPS 02 - Install the requirements

```bash
pip install -r requirements.txt
```

#### STEPS 03 -Set Up PostgreSQL Database

##### Set Up PostgreSQL Database on Railway

Step 1: Create an account on [railway.app](https://railway.app/)

Step 2: In your dashboard (railway.app/dashboard) click "+ New Project" and select "Provision PostgresSQL". It should take a few seconds for your database to be ready.

Step 3: Once your database is ready, select the new database and go to the "Connect" tab. Here you will see your "Postgres Connection URL".

This connection URL may seem like a bunch of random character's so lets extract all the values from this url by selecting the "Variables" tab if you want a more user friendly version of this connection.

Go ahead and stick to the default values provided and update our connection in our django settings.py file.

```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '<PGDATABASE>',
        'USER': '<PGUSER>',
        'PASSWORD': '<PGPASSWORD>',
        'HOST': '<PGHOST>',
        'PORT': '<PGPORT>',
    }
}

```


#### STEPS 04 - Run Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

#### STEPS 05 - Start the Development Server

```bash
python manage.py runserver
```

## API Endpoints
The following API endpoints are available:

| Method | Endpoint                       | Description                                   |
|--------|-------------------------------|-----------------------------------------------|
| POST   | `/register/`                  | Registers a new user                          |
| POST   | `/student/register/`          | Registers a new student                       |
| POST   | `/teacher/register/`          | Registers a new teacher                       |
| POST   | `/login/`                     | Authenticates a user and returns a token     |
| GET    | `/students/`                  | Retrieves a list of all registered students   |
| GET    | `/teachers/`                  | Retrieves a list of all registered teachers   |


Cheers and Happy Coding :)
