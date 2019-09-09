# PhotoDB
FROM python:3
MAINTAINER Jonathan Gazeley
# Install Python and Package Libraries
RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean
#RUN apt-get install -y \
#    libffi-dev \
#    libssl-dev \
#    libmysqlclient-dev \
#    libxml2-dev \
#    libxslt-dev \
#    libjpeg-dev \
#    libfreetype6-dev \
#    zlib1g-dev \
#    net-tools \
#    vim
# Project Files and Settings
ARG PROJECT=photodb
ARG PROJECT_DIR=/var/www/${PROJECT}
RUN mkdir -p $PROJECT_DIR
WORKDIR $PROJECT_DIR
COPY requirements.txt .
RUN pip install -r requirements.txt

# Server
EXPOSE 8000
STOPSIGNAL SIGINT
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
