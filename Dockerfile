FROM python:3.10-slim

WORKDIR app/

RUN apt update \
    && apt install -y gcc libpq-dev curl \
    && apt-get autoclean && apt-get autoremove \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . /app
