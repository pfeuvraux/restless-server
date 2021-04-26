from pydantic import BaseModel
from enum import Enum
from typing import Any

class Login_SrpPhase(str, Enum):

  challenge = "challenge"
  verify = "verify"

class Login_In(BaseModel):

  username: str
  srp_params: list[str]

class Login_Out(BaseModel):

  token: str


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
