from pydantic import BaseModel

class HTTP_409_CODE_Model(BaseModel):

  detail: str

class Register_In(BaseModel):

  username: str
  srp_salt: str
  srp_verifier: str

class Register_Out(BaseModel):

  message: str
