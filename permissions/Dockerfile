FROM python:3.10

RUN mkdir -p /permissions/app

COPY ./permissions/requirements.txt /permissions/requirements.txt

COPY ./permissions /permissions/app

RUN pip install -r permissions/requirements.txt

WORKDIR /permissions/app