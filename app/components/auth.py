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
      srp_verifier=self.user.srp_verifier,
      kek_salt=self.user.kek_salt,
      cek=self.user.cek
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

    if user_attributes is None:
      raise HTTPException(
        status_code=400
      )

    srp_phase = getattr(self, srp_phase)
    return srp_phase(user_attributes, self.user.srp_params)


  def srp_init(self, user_attrs, params):

    salt = user_attrs.srp_salt
    return {
      "salt": salt
    }


  def srp_challenge(self, user_attrs, params):

    return {}

  def srp_verify(self, user_attrs, params):
    return {
      "token": "verify"
    }
