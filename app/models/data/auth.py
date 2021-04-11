from pydantic import BaseModel

class UserCommon(BaseModel):

  username: str
  password: str

class UserLogin_Out(BaseModel):

  token: str
