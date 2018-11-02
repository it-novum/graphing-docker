FROM alpine:latest

ENV PYTHONPATH="/opt/graphite/lib/:/opt/graphite/webapp/"

RUN apk --no-cache add python2 python2-dev gcc libc-dev py2-pip libffi-dev py2-gunicorn cairo

RUN pip install --no-binary=:all: https://github.com/graphite-project/whisper/tarball/master https://github.com/graphite-project/carbon/tarball/master https://github.com/graphite-project/graphite-web/tarball/master "whitenoise==3.*"

RUN mkdir -p /var/lib/graphite/whisper /etc/uwsgi /opt/graphite/webapp/graphite

COPY wsgi.py /opt/graphite/conf/
COPY local_settings.py /opt/graphite/webapp/graphite/local_settings.py
COPY run.sh /run.sh

##RUN /usr/bin/django-admin collectstatic --settings=graphite.settings

VOLUME /var/lib/graphite/whisper

EXPOSE 8080

CMD ["/bin/sh", "-e", "/run.sh"]

