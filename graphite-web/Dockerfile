FROM alpine:latest AS build

#ENV PYTHONPATH="/opt/graphite/lib/:/opt/graphite/webapp/"

RUN apk --no-cache add python3 libffi py3-gunicorn cairo py3-setuptools

RUN apk --no-cache add python3-dev gcc libc-dev py3-pip libffi-dev py3-gunicorn cairo py3-mysqlclient

RUN pip3 install wheel urllib3

# the touch fixes the missing __init__.py file from the broken zope.interface package ...
RUN pip3 install --no-binary=:all: --prefix=/opt/graphite https://github.com/graphite-project/whisper/archive/1.1.6.zip https://github.com/graphite-project/carbon/archive/1.1.6.zip https://github.com/graphite-project/graphite-web/archive/1.1.6.zip "whitenoise==3.*"


FROM alpine:latest

ENV PYTHONPATH="/opt/graphite/lib/:/opt/graphite/lib/python3.8/site-packages/:/opt/graphite/webapp/"

RUN apk --no-cache add python3 libffi py3-gunicorn cairo py3-setuptools py3-mysqlclient py3-pip

RUN pip3 install urllib3

RUN mkdir -p /var/lib/graphite/whisper /etc/uwsgi /opt/graphite/webapp/graphite

COPY wsgi.py /opt/graphite/conf/
#COPY local_settings.py /opt/graphite/lib/graphite/local_settings.py

# Link generated config
RUN mkdir -p /opt/graphite/lib/graphite
RUN ln -sf /etc/carbon/local_settings.py /opt/graphite/lib/graphite/local_settings.py

COPY run.sh /run.sh
COPY --from=build /opt/graphite /opt/graphite

VOLUME /var/lib/graphite/whisper
EXPOSE 8080

CMD ["/bin/sh", "-e", "/run.sh"]


