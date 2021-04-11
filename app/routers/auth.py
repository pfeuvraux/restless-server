from fastapi import APIRouter, HTTPException
from fastapi import status as http_codes
from app.utils.logger import logger
from app.models.data import auth as auth_datamodel
from app.models.db import auth as auth_dbmodel

router = APIRouter(
  prefix="/auth",
  tags=["auth"]
)

@router.post("/login",
  response_model=auth_datamodel.UserLogin_Out,
  status_code=http_codes.HTTP_200_OK
)
async def login(user: auth_datamodel.UserCommon):
  pass

@router.post('/register',
  status_code=http_codes.HTTP_201_CREATED,
)
async def register(user: auth_datamodel.UserCommon):
  pass
