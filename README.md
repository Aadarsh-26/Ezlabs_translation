🚀 EZ Labs Translation Service – Backend (Django + DRF + Celery)

This project implements the Low-Level Design (LLD) assignment for a backend engineering role at EZ Labs.
The system provides an end-to-end translation workflow with features such as:

Translation job submission

Background processing using Celery

Priority-based queues (high/medium/low)

JWT authentication

Rate limiting

Job status tracking

Translation result retrieval

Dockerized deployment

This project demonstrates strong backend architecture, scalability design, and clean REST API implementation.

📘 Project Overview

The goal of the system is to allow users to:

Upload a document for translation

Choose source & target languages

Have the translation processed asynchronously

Track the progress/state of the job

Retrieve the translated output

Celery + Redis is used for background processing, ensuring non-blocking performance and the ability to scale workers independently.

🧱 Tech Stack

Python 3.11+

Django 4+

Django REST Framework

Celery 5+

Redis (broker + backend)

PostgreSQL

JWT Authentication

Docker & docker-compose


pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
celery -A ezlabs_translation worker --loglevel=info -Q translation_high,translation_default,translation_low
docker-compose up --build
docker-compose exec web python manage.py migrate

🔍 Rate Limiting

The system enforces API throttling to protect resources:

Scope	Limit
user	200 requests/min
anon	10 requests/min
translation_submit	10 submissions/min

This ensures fairness and prevents spam translation jobs.
