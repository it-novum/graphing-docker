# grafana-docker

Dockerfiles for Graphing Backend of [openITCOCKPIT](https://github.com/it-novum/openITCOCKPIT). 🐳

## Local usage
````
git clone https://github.com/it-novum/graphite-docker.git
cd graphite-docker
````

### Build `graphite-web` image
````
cd graphite-web/
docker build --rm \
  --build-arg HTTP_PROXY=http://172.16.101.111:8080 --build-arg HTTPS_PROXY=http://172.16.101.111:8080 \
  --build-arg http_proxy=http://172.16.101.111:8080 --build-arg https_proxy=http://172.16.101.111:8080 \
  -t openitcockpit/graphite-web:latest .
````
### Run `graphite-web` container
````
cd graphite-web
docker run -t -i --rm \
  --name=graphite-web
  -p 127.0.0.1:8086:8080 \
  openitcockpit:graphite-web-latest
````


### Build `carbon-c-relay` image
````
cd carbon-c-relay/
docker build --rm \
  --build-arg HTTP_PROXY=http://172.16.101.111:8080 --build-arg HTTPS_PROXY=http://172.16.101.111:8080 \
  --build-arg http_proxy=http://172.16.101.111:8080 --build-arg https_proxy=http://172.16.101.111:8080 \
  -t openitcockpit/carbon-c-relay:latest .
````

#### Run `carbon-c-relay` container

````
docker run -t -i --rm \
  -p 127.0.0.1:2003:2003 \
  --name=carbon-c-relay \
  --expose=2003
  -v /etc/openitcockpit/grafana:/etc/openitcockpit/grafana \
  openitcockpit/carbon-c-relay:latest -f /etc/carbon-c-relay/carbon-c-relay.conf -T 600 -w 4 -p 2003
````


### Build `carbon-cache` image
````
cd carbon-cache/
docker build --rm \
  --build-arg HTTP_PROXY=http://172.16.101.111:8080 --build-arg HTTPS_PROXY=http://172.16.101.111:8080 \
  --build-arg http_proxy=http://172.16.101.111:8080 --build-arg https_proxy=http://172.16.101.111:8080 \
  -t openitcockpit/carbon-cache:latest .
````
### Run `carbon-cache` container
````
cd carbon-cache/
docker run -t -i --rm \
  --name=carbon-cache01 \
  -v /etc/openitcockpit/grafana:/etc/openitcockpit/carbone \
  openitcockpit/carbon-cache:latest -f /etc/carbon-c-relay/carbon-c-relay.conf -T 600 -w 4 -p 2003
````














## Builds


# License
[MIT License](https://github.com/it-novum/graphite-docker/blob/master/LICENSE)
