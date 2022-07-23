FROM python:3.10

RUN mkdir -p /permissions-service/app

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

COPY ./permissions-service/requirements.txt /permissions-service/requirements.txt

COPY ./permissions-service /permissions-service/app

RUN pip install -r permissions-service/requirements.txt

WORKDIR /permissions-service/app