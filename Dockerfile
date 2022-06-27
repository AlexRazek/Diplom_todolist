FROM python:3.10-slim

WORKDIR app/
RUN apt update && apt install -y gcc libpq-dev
#RUN apt-get clean && apt-get update
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . /app
CMD python3 manage.py runserver 0.0.0.0:8000