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

def create_user(username: str, password: str):

  user_id = uuid4()

  User_by_id_Model.objects.create(
    user_id=user_id,
    username=username,
    password=password
  )

  User_by_username_Model.objects.create(
    user_id=user_id,
    username=username,
    password=password
  )

  return True
