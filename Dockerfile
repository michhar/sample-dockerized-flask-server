FROM ubuntu:latest
MAINTAINER M. Harris

RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential

COPY /src/. .

RUN pip3 install -r requirements_web.txt
RUN pip3 install gunicorn

ENV FLASK_APP app.py

EXPOSE 8080
CMD ["gunicorn"  , "-b", "0.0.0.0:8080", "app:app"]