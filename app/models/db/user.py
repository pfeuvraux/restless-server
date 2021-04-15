from app.utils.logger import logger
from app.models.db import (
  User_by_username_Model,
  User_by_id_Model
)
from uuid import uuid4

def get_user_attributes_by_username(username: str):

  res = User_by_username_Model.objects.filter(username=username)
  try:
    return res.get()
  except User_by_username_Model.DoesNotExist as err:
    return None
  except Exception as err:
    raise Exception(err)

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
