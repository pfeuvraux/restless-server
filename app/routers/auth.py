from fastapi import APIRouter, HTTPException
from fastapi import status as http_codes
from app.utils.logger import logger
from app.models.data import auth as auth_datamodel
from app.components.auth import RegisterUser

router = APIRouter(
  prefix="/auth",
  tags=["auth"]
)

@router.post("/login",
  response_model=auth_datamodel.Login_Out,
  status_code=http_codes.HTTP_200_OK
)
def login(user: auth_datamodel.Login_In):
  pass

@router.post('/register',
  status_code=http_codes.HTTP_201_CREATED,
  response_model=auth_datamodel.Register_Out,
  responses={
    409: {
      "description": "User already exists",
      "model": auth_datamodel.Register_HTTP_409
    }
  }
)
def register(user: auth_datamodel.Register_In):

  register_user = RegisterUser(model=user)
  res = register_user()

  return res
