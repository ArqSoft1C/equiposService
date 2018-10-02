FROM python:2.7

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY . /code/
ADD requirements.txt /code/
RUN pip install -r requirements.txt && python manage.py migrate
EXPOSE 4000
CMD ["python", "manage.py", "runserver", "0.0.0.0:4000"]