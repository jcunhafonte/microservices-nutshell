FROM python:3.10

RUN mkdir -p /insights-service/app

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

COPY ./insights-service/requirements.txt /insights-service/requirements.txt

COPY ./insights-service /insights-service/app

RUN pip install --no-cache-dir --upgrade -r /insights-service/requirements.txt

WORKDIR /insights-service/app