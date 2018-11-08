#!/bin/sh

/usr/bin/django-admin migrate --settings=graphite.settings --run-syncdb

cd /opt/graphite/conf
exec /usr/bin/gunicorn -w 4 -b 0.0.0.0:8080 wsgi:application 

