FROM python:3.12.2

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 10000

CMD [ "python", "manage.py", "runserver", "10000" ]