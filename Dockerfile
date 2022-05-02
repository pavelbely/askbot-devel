#
# WARNING: this Docker file is not tested with the current askbot-setup script.
# most likely at least this file will need to be adapted to make it work.
# if you can help - please make explain what you want to do in the issues
# section of the repository and once your contribution is accepted - make a pull request.
#
#----------------------------------------------------
# This Dockerifle builds a simple Askbot installation
#
# It makes use of environment variables:
# 1. DATABASE_URL See https://github.com/kennethreitz/dj-database-url for details
# 2. SECRET_KEY for making hashes within Django.
# 3. ADMIN_PASSWORD used for creating a user named "admin"
# 4. NO_CRON set this to "yes" to disable the embedded cron job.
#
# Make sure to *+always* start the container with the same SECRET_KEY.
#
# Start with something like
#
# docker run -e 'DATABASE_URL=sqlite:////askbot-site/askbot.db' -e "SECRET_KEY=$(openssl rand 14 | base64)" -e ADMIN_PASSWORD=admin -p 8080:80 askbot/askbot:latest
#
# User uploads are stored in **/askbot_site/askbot/upfiles** . I'd recommend to make it a kubernetes volume.

FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1

ADD askbot_requirements.txt /askbot_requirements.txt

#RUN apt-get update && apt-get -y install cron git \
RUN apk add --update --no-cache git py3-cffi \
	gcc g++ git make unzip mkinitfs kmod mtools squashfs-tools py3-cffi \
	libffi-dev linux-headers musl-dev libc-dev openssl-dev \
	python3-dev zlib-dev libxml2-dev libxslt-dev jpeg-dev \
        postgresql-dev zlib jpeg libxml2 libxslt postgresql-libs \
    && python -m pip install --upgrade pip \
    && pip install -r /askbot_requirements.txt \
    && pip install psycopg2 \
    && pip install 'django-appconf==1.0.3'

RUN pip install unidecode

ADD . /application

RUN cd /application && python setup.py install --single-version-externally-managed --root=/

WORKDIR /application/recovenn

CMD ["sh", "-c", "python manage.py runserver 0.0.0.0:${PORT}"]
