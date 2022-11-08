FROM python:3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# install dependencies
RUN pip install --upgrade pip
COPY cost_control/requirements.txt .
RUN pip install -r requirements.txt
# copy project
COPY cost_control .
CMD ["python","manage.py","migrate"]