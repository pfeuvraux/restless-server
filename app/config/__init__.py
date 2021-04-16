import os
from yaml import (
  SafeLoader,
  load
)
from pydantic import (
  BaseSettings,
  BaseModel
)
from typing import Any
from pathlib import Path

def default_yaml_source_settings(settings: BaseSettings):

  curr_dir = os.path.dirname(os.path.abspath(__file__))

  return load(Path(f"{curr_dir}/defaults.yml").read_text('utf-8'))

class Database_Config(BaseModel):

  hosts: list[str] = ['localhost']
  port: int = 9042
  keyspace: str = "restless"
  protocol_version: int = 4

class Settings(BaseSettings):

  database: Database_Config = Database_Config()

  class Config:

    @classmethod
    def customise_sources(
      cls,
      init_settings,
      env_settings,
      file_secret_settings
    ):
      return (
        default_yaml_source_settings,
        init_settings
      )


settings = Settings()
