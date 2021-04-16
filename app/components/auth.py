from fastapi import HTTPException, status
from app.models.db.user import (
  describe_user_by_username,
  create_user
)

class RegisterUser:

  def __init__(self, model):
    self.user = model

  def __call__(self):

    if self.user_exists():
      raise HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail="User already exists"
      )

    if not self.user.username.isalnum():
      raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Username must be alphanumeric"
      )

    create_user(
      username=self.user.username,
      password=self.user.password
    )

    return {
      "message": "User successfully registered"
    }


  def user_exists(self) -> bool:

    user_attributes = describe_user_by_username(self.user.username)
    if user_attributes is not None:
      return True
    return False
