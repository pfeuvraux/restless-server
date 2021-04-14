# //Init DB session

from . import (
  auth
)

from cassandra.cluster import Cluster
from app.config import default_settings

__cluster = Cluster(
  default_settings['database']['hosts'],
  port=default_settings['database']['port']
)
scylladb = __cluster.connect(
  default_settings['database']['keyspace']
)
