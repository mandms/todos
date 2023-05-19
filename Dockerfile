FROM python:3.7.3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /todos

COPY ./requirements.txt /todos/requirements.txt

RUN pip install -r /todos/requirements.txt

COPY . /todos

EXPOSE 8000
CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
