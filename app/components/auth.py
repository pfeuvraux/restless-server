from fastapi import HTTPException, status
from app.models.db.user import (
  get_user_attributes_by_username,
  create_user
)

class RegisterUser:

  def __init__(self, model):
    self.user = model

  def __call__(self):

    if not self.user.username.isalnum():
      raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Username must be alphanumeric"
      )

    user_attributes = get_user_attributes_by_username(self.user.username)
    if user_attributes is not None:
      raise HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail="User already exists"
      )

    create_user(
      username=self.user.username,
      password=self.user.password
    )

    return {
      "message": "User successfully registered"
    }
