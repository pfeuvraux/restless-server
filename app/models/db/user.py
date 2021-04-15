from app.models.db import ScyllaQuery
from uuid import uuid4

def get_user_attributes_by_username(username: str):

  cql_statement = "SELECT username FROM user_by_username WHERE username=?;"
  query = ScyllaQuery(
    statement=cql_statement,
    params=[username]
  )
  return query.run()

def create_user(username: str, password: str):

  user_id = uuid4()

  cql_statement = f"INSERT INTO user_by_id (user_id, username, password) VALUES (?, ?, ?);"
  query = ScyllaQuery(
    statement=cql_statement,
    params=[
      user_id,
      username,
      password
    ]
  )

  query.run()


  cql_statement = f"INSERT INTO user_by_username (user_id, username, password) VALUES (?, ?, ?);"
  query = ScyllaQuery(
    statement=cql_statement,
    params=[
      user_id,
      username,
      password
    ]
  )

  query.run()

  pass


