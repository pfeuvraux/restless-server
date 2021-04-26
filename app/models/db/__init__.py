# //Init DB session

import uuid
from cassandra.cqlengine.models import Model
from cassandra.cqlengine.management import sync_table
from cassandra.cqlengine import (
  columns,
  connection
)
from app.utils.logger import logger
from app.config import settings

logger.info('Connecting to database...')
logger.debug('Contact points:')
logger.debug(settings.database.hosts)


"""USER MODELS"""

class User_by_id_Model(Model):
  __table_name__ = "user_by_id"

  user_id = columns.UUID(primary_key=True, default=uuid.uuid4, required=True)
  username = columns.Text(required=True)
  srp_salt = columns.Text(required=True)
  srp_verifier = columns.Text(required=True)
  kek_salt = columns.Text(required=True)
  cek = columns.Text(required=True)

class User_by_username_Model(Model):
  __table_name__ = "user_by_username"

  username = columns.Text(primary_key=True, required=True)
  user_id = columns.UUID(required=True)
  srp_salt = columns.Text(required=True)
  srp_verifier = columns.Text(required=True)
  kek_salt = columns.Text(required=True)
  cek = columns.Text(required=True)

"""END USER MODELS"""


connection.setup(
  settings.database.hosts,
  settings.database.keyspace,
  port=settings.database.port,
  protocol_version=settings.database.protocol_version
)
tables = [
  User_by_id_Model,
  User_by_username_Model
]

for table in tables:
  logger.debug(f"Syncing {table.__table_name__}...")
  sync_table(table)
logger.debug('Done')
