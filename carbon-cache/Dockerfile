FROM alpine:latest

ENV PYTHONPATH="/opt/graphite/lib/:/opt/graphite/webapp/"

RUN apk --no-cache add python2 python2-dev gcc libc-dev py2-pip libffi-dev

RUN pip install --no-binary=:all: https://github.com/graphite-project/whisper/tarball/master https://github.com/graphite-project/carbon/tarball/master https://github.com/graphite-project/graphite-web/tarball/master

RUN mkdir -p /etc/carbon /var/lib/graphite/whisper

VOLUME /etc/carbon
VOLUME /var/lib/graphite/whisper
EXPOSE 2003

CMD ["/opt/graphite/bin/carbon-cache.py", "--config=/etc/carbon/carbon.conf", "--nodaemon", "start"]

