FROM python:3.11-slim-bullseye

WORKDIR /app

RUN apt-get update
RUN apt-get install -y vim gcc
RUN pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt


COPY . .

EXPOSE 8000

ENTRYPOINT [ "sh", "/app/devops/bootup.sh" ]