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
- docker-compose up
- --
Start cron/remove
- python manage.py crontab add
- python manage.py crontab remove
- --
- Documentation for the API is made in Swagger
- --
- Deploy for Heroku https://costcontrolapp.herokuapp.com/
- User registration via gmail is required.
- After that you will receive a link to go through.
- After which you must log in.
- And Autorize. 

