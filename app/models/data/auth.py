from pydantic import BaseModel
from enum import Enum
from typing import (
  Dict,
  Any,
  Optional
)

class Login_SrpPhase(str, Enum):

  challenge = "challenge"
  verify = "verify"
  init = "init"

class Login_In(BaseModel):

  username: str
  srp_params: Optional[Any]

class Register_HTTP_409(BaseModel):

  detail: str

class Register_In(BaseModel):

  username: str
  srp_salt: str
  srp_verifier: str
  kek_salt: str
  cek: str

class Register_Out(BaseModel):

  message: str
