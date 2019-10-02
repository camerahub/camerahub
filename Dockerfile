# PhotoDB
FROM python:3
LABEL maintainer "Jonathan Gazeley"

RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean

# Project Files and Settings
ARG PROJECT=photodb
ARG PROJECT_DIR=/var/www/${PROJECT}
RUN mkdir -p $PROJECT_DIR
ADD . $PROJECT_DIR
WORKDIR $PROJECT_DIR
RUN pip install .

# Run migrations
RUN python manage.py migrate

# Server
EXPOSE 8000
STOPSIGNAL SIGINT
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
