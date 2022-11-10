# Cost control
Cost control for your life
---

Venv:
- virtualenv --python python3.8 venv
- source venv/bin/activate
- --
Run:
- python manage.py makemigrations/migrate/runserver
- --
Or Docker:
- docker-compose build
-  docker-compose up
- --
Start cron/remove
- python manage.py crontab add
- python manage.py crontab remove
- --
- Documentation for the API is made in Swagger
- --



