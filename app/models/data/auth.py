from pydantic import BaseModel

class Login_In(BaseModel):

  TBD: str # TO BE DEFINED

class Login_Out(BaseModel):

  token: str


class Register_HTTP_409(BaseModel):

  detail: str

class Register_In(BaseModel):

  username: str
  srp_salt: str
  srp_verifier: str

class Register_Out(BaseModel):

  message: str
