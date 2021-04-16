from pydantic import BaseModel

class HTTP_409_CODE_Model(BaseModel):

  detail: str

class UserCommon(BaseModel):

  username: str
  password: str

class UserLogin_Out(BaseModel):

  token: str

class Register_Out(BaseModel):

  message: str
