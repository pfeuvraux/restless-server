# FIXME: ARGPARSE + CREATE KEYSPACE + SLEEP BEFORE ANYTHING

from cassandra.cluster import Cluster

cluster = Cluster(['localhost'])
session = cluster.connect()

keyspace_name = "restless"

session.execute(
  f"CREATE KEYSPACE IF NOT EXISTS {keyspace_name} WITH replication = {{'class': 'SimpleStrategy', 'replication_factor': '1'}};"
)
