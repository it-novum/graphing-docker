FROM alpine:latest AS build

ENV \
 TERM=xterm \
 C_RELAY_VERSION="3.4" 

RUN mkdir -p /build/carbon-c-relay /opt/carbon-c-relay

WORKDIR /build

RUN apk --no-cache add gcc curl g++ git make musl-dev tar gzip wget

RUN wget https://github.com/grobian/carbon-c-relay/archive/v${C_RELAY_VERSION}.tar.gz && \
 tar -xf v${C_RELAY_VERSION}.tar.gz && \
 cd carbon-c-relay-${C_RELAY_VERSION} && \
 ./configure --prefix=/opt/carbon-c-relay && \
 make && \
 make install

FROM alpine:latest

ENV \
 TERM=xterm \
 C_RELAY_VERSION="3.4" 

RUN mkdir -p /opt/carbon-c-relay /etc/carbon-c-relay

COPY --from=build /opt/carbon-c-relay/. /opt/carbon-c-relay/

CMD ["/opt/carbon-c-relay/bin/relay"]


