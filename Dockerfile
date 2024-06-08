FROM python:3.12.2

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "python", "manage.py", "runserver" ]