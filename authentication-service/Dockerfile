FROM python:3.10

RUN mkdir -p /authentication-service/app

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

COPY ./authentication-service/requirements.txt /authentication-service/requirements.txt

COPY ./authentication-service /authentication-service/app

RUN pip install --no-cache-dir --upgrade -r /authentication-service/requirements.txt

WORKDIR /authentication-service/app