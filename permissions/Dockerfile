FROM python:3.10

RUN mkdir -p /permissions/app

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

COPY ./permissions/requirements.txt /permissions/requirements.txt

COPY ./permissions /permissions/app

RUN pip install -r permissions/requirements.txt

WORKDIR /permissions/app