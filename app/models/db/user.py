from app.utils.logger import logger
from app.models.db import (
  User_by_username_Model,
  User_by_id_Model
)
from uuid import uuid4

def describe_user_by_username(username: str):

  res = User_by_username_Model.objects.filter(username=username)
  try:
    return res.get()
  except User_by_username_Model.DoesNotExist:
    return None

def create_user(
  username: str,
  srp_salt: str,
  srp_verifier: str,
  kek_salt: str,
  cek: str
) -> None:

  user_id = uuid4()

  query_params = {
    "user_id": user_id,
    "username": username,
    "srp_salt": srp_salt,
    "srp_verifier": srp_verifier,
    "kek_salt": kek_salt,
    "cek": cek
  }
  User_by_id_Model.objects.create(**query_params)
  User_by_username_Model.objects.create(**query_params)

  pass
