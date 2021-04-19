from fastapi import HTTPException, status
from fastapi import status
from app.models.db.user import (
  describe_user_by_username,
  create_user
)
import srp
from base64 import b64decode

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
      srp_salt=self.user.srp_salt,
      srp_verifier=self.user.srp_verifier
    )

    return {
      "message": "User successfully registered"
    }


  def user_exists(self) -> bool:

    user_attributes = describe_user_by_username(self.user.username)
    if user_attributes is not None:
      return True
    return False

class LoginUser:

  def __init__(self, model, srp_phase):
    self.user = model
    self.srp_phase = srp_phase

  def __call__(self):

    srp_phase = f"srp_{self.srp_phase}"

    user_attributes = describe_user_by_username(
      username=self.user.username
    )

    route = getattr(self, srp_phase)
    return route(
      salt=b64decode(user_attributes.srp_salt).decode('utf-8'),
      vkey=b64decode(user_attributes.srp_verifier).decode('utf-8')
    )

  def srp_challenge(self, salt, vkey):


    return {
      "token": "challenge"
    }

  def srp_verify(self, salt, vkey):
    return {
      "token": "verify"
    }
