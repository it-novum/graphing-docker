FROM alpine:latest

ENV \
 TERM=xterm \
 C_RELAY_VERSION="3.4" 

RUN apk --no-cache add gcc curl g++ git make musl-dev tar gzip wget

RUN mkdir -p /opt/carbon-c-relay \
mkdir -p /etc/carbon-c-relay

RUN wget https://github.com/grobian/carbon-c-relay/archive/v${C_RELAY_VERSION}.tar.gz && \
 tar -xf v${C_RELAY_VERSION}.tar.gz && \
 cd carbon-c-relay-${C_RELAY_VERSION} && \
 ./configure --prefix=/opt/carbon-c-relay && \
 make && \
 make install && \
 rm -rf /tmp/* /var/cache/apk/*


CMD ["/opt/carbon-c-relay/bin/relay"]
