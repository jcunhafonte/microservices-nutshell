FROM python:3.10

RUN mkdir -p /insights/app

COPY ./insights/requirements.txt /insights/requirements.txt

COPY ./insights /insights/app

RUN pip install --no-cache-dir --upgrade -r /insights/requirements.txt

WORKDIR /insights/app