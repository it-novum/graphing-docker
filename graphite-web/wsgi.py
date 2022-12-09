import sys

# Packport of https://github.com/graphite-project/graphite-web/pull/2333
# Configure of WhiteNoise 4.1.4 is done by middleware in app_settings.py
# http://whitenoise.evans.io/en/stable/changelog.html#v4-0
# See for old WhiteNoise 3.x version: https://github.com/it-novum/graphing-docker/blob/10f22f6c251d2b6ef2cc33d5c5e2a41d1ae5d3f7/graphite-web/wsgi.py


sys.path.append('/opt/graphite/webapp')

from graphite.wsgi import application as graphapp
application = graphapp
