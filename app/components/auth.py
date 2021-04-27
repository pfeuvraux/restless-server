from fastapi import HTTPException, status
from fastapi import status
from app.models.db.user import (
  describe_user_by_username,
  create_user
)
import srp
from base64 import (
  b64decode,
  b64encode
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
        status_code=400,
        detail="User doesn't exist."
      )

    srp_phase = getattr(self, srp_phase)
    return srp_phase(user_attributes, self.user.srp_params)


  def srp_init(self, user_attrs, params):

    salt = user_attrs.srp_salt
    return {
      "salt": salt
    }


  def srp_challenge(self, user_attrs, params):

    """Challenge phase

    1. Gets A # base64-encoded
    2. Computes
    3. Gives B
    """

    srp.rfc5054_enable()

    A = b64decode(params['srpA'])
    srp_salt = b64decode(user_attrs.srp_salt)
    srp_verifier = b64decode(user_attrs.srp_verifier)


    srp_instance = srp.Verifier(user_attrs.username, srp_salt, srp_verifier, A, ng_type=srp.NG_4096, hash_alg=srp.SHA256)
    s, B = srp_instance.get_challenge()

    if s is None or B is None:
      raise HTTPException(
        status_code=401,
        detail="Failed SRP challenge."
      )

    return {
      "s": b64encode(s).decode('utf-8'),
      "B": b64encode(B).decode('utf-8')
    }

  def srp_verify(self, user_attrs, srp_params):

    """Verify phase

    1. Gets M1
    2. Computes
    3. Gives M2
    """

    srp.rfc5054_enable()

    A = b64decode(srp_params['srpA'])
    M1 = b64decode(srp_params['M1'])

    srp_salt = b64decode(user_attrs.srp_salt)
    srp_verifier = b64decode(user_attrs.srp_verifier)

    srp_instance = srp.Verifier(user_attrs.username, srp_salt, srp_verifier, A, ng_type=srp.NG_4096, hash_alg=srp.SHA256)

    M2 = srp_instance.verify_session(M1)

    if M2 is None:
      raise HTTPException(
        status_code=400,
        detail="SRP M2 parameter is not valid."
      )
    return {
      "M2": b64encode(M2).decode('utf-8')
    }
