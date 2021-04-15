# //Init DB session

from cassandra.cluster import Cluster
from app.config import default_settings

__cluster = Cluster(
  default_settings['database']['hosts'],
  port=default_settings['database']['port']
)
scylladb = __cluster.connect(
  default_settings['database']['keyspace']
)

class ScyllaQuery:

  def __init__(self, statement: str, params: list):
    self.prep_statement = scylladb.prepare(statement)
    self.cql_values = params

  def run(self):

    future = scylladb.execute_async(
      self.prep_statement,
      self.cql_values
    )
    return future.result()
