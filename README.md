
Dockerfiles for Graphing Backend of [openITCOCKPIT](https://github.com/it-novum/openITCOCKPIT). 🐳

## Run via `docker-compose`
````
git clone https://github.com/it-novum/graphite-docker.git
cd graphite-docker

#Use loca docker-compose file
mv docker-compose_local.yml docker-compose.yml


docker-compose up
````

## Local usage
````
git clone https://github.com/it-novum/graphite-docker.git
cd graphite-docker
````

### Copy required files
````
mkdir -p /etc/openitcockpit/grafana
mkdir -p /etc/openitcockpit/carbon

echo admin > /etc/openitcockpit/grafana/admin_password
cp grafana/grafana.ini /etc/openitcockpit/grafana/

cp carbon-c-relay/carbon-c-relay.conf /etc/openitcockpit/carbon/
cp carbon-cache/carbon.conf /etc/openitcockpit/carbon/
cp carbon-cache/storage-aggregation.conf /etc/openitcockpit/carbon/
cp carbon-cache/storage-schemas.conf /etc/openitcockpit/carbon/
cp graphite-web/local_settings.py /etc/openitcockpit/carbon/
cp graphite-web/wsgi.py /etc/openitcockpit/carbon/
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
  openitcockpit:graphite-web
````

### Run a shell inside the `graphite-web` container
````
cd graphite-web
docker run -t -i --rm \
  --name=graphite-web
  -p 127.0.0.1:8086:8080 \
  openitcockpit:graphite-web /bin/sh
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


### Run `grafana` container
````
docker run -t -i --rm \
  -p 127.0.0.1:3033:3033 \
  --name=shadow_grafana \
  -e "GF_SECURITY_ADMIN_PASSWORD=admin" \
  -e "GF_PATHS_CONFIG=/etc/openitcockpit/grafana/grafana.ini" \
  -e "GF_PATHS_DATA=/var/lib/grafana" \
  -e "GF_PATHS_HOME=/usr/share/grafana" \
  -e "GF_PATHS_LOGS=/var/log/grafana" \
  -e "GF_PATHS_PLUGINS=/var/lib/grafana/plugins" \
  -e "GF_PATHS_PROVISIONING=/etc/grafana/provisioning" \
  -v grafana-data:/var/lib/grafana \
  -v /etc/openitcockpit/grafana:/etc/openitcockpit/grafana \
  grafana/grafana
````


# License
[MIT License](https://github.com/it-novum/graphite-docker/blob/master/LICENSE)
