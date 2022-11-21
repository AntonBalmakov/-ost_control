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


- --
- Use a known working email/ Use gmail.com
- --
![image](https://user-images.githubusercontent.com/61959404/203065792-d6eb482d-eedc-4f3a-9759-edbfe36ad235.png)
