FROM alpine:latest AS build

#ENV PYTHONPATH="/opt/graphite/lib/:/opt/graphite/webapp/"

RUN apk --no-cache add python3 libffi

RUN apk --no-cache add python3-dev gcc libc-dev py3-pip libffi-dev

RUN pip3 install wheel urllib3

RUN pip3 install --no-binary=:all: --prefix=/opt/graphite https://github.com/graphite-project/whisper/tarball/master https://github.com/graphite-project/carbon/tarball/master https://github.com/graphite-project/graphite-web/tarball/master


FROM alpine:latest

ENV PYTHONPATH="/opt/graphite/lib/:/opt/graphite/lib/python3.8/site-packages/:/opt/graphite/webapp/"

RUN apk --no-cache add python3 py3-pip libffi

RUN pip3 install urllib3

RUN mkdir -p /etc/carbon /var/lib/graphite/whisper

VOLUME /etc/carbon
VOLUME /var/lib/graphite/whisper
EXPOSE 2003

COPY --from=build /opt/graphite /opt/graphite

CMD ["/opt/graphite/bin/carbon-cache.py", "--config=/etc/carbon/carbon.conf", "--nodaemon", "start"]


