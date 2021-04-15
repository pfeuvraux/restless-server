from pydantic import (
  BaseSettings,
  BaseModel
)
from typing import Any

class Config_Database(BaseModel):

  hosts: list[str] = ["172.22.0.2"]
  port: int = 9042
  keyspace: str = "restless"
  protocol_version: int = 4

class Settings(BaseSettings):

  database: Config_Database = Config_Database()

  class Config:
      env_prefix = "restless_env_"


settings = Settings()
