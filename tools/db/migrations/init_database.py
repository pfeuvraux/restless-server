import os
from yaml import load, SafeLoader
from cassandra.cluster import Cluster
from pydantic import BaseModel
from time import sleep
from json import load as jsonload

curr_dir = os.path.dirname(os.path.abspath(__file__))
project_path = f"{curr_dir}/../../.."

class DatabaseSettings(BaseModel):

  hosts: list[str]
  port: str
  keyspace: str

def setup_scylla_client():

  with open(f"{project_path}/app/config/defaults.yml") as conf_fd:
    defaults = load(conf_fd, Loader=SafeLoader)
    dbsettings = DatabaseSettings(**defaults['database'])
    conf_fd.close()

  __cluster = Cluster(
    dbsettings.hosts,
    port=dbsettings.port
  )
  return __cluster.connect(), dbsettings.keyspace

def create_tables():

  with open(f"{curr_dir}/tables.json", "r") as tables_fd:
    tables_list = jsonload(tables_fd)
    tables_fd.close()

  for table in tables_list:
    table_name = table['name']
    cols = table['cols']
    cols_text = ""
    for col in cols:
      cols_text = f"{cols_text}{col['name']} {col['type']}, "

    cql_statement = f"CREATE TABLE IF NOT EXISTS {table_name}( {cols_text} );"
    print(cql_statement)

    scyllaclient.execute(cql_statement)


def create_keyspace(name: str) -> None:

  scyllaclient.execute(
    f"CREATE KEYSPACE IF NOT EXISTS {name} WITH replication = {{'class': 'SimpleStrategy', 'replication_factor': '1'}};"
  )

if __name__ == "__main__":

  scyllaclient, keyspace = setup_scylla_client()
  create_keyspace(name=keyspace)
  scyllaclient.set_keyspace(keyspace)

  create_tables()
