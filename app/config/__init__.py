import os
from pydantic import BaseModel
from yaml import load, SafeLoader


__curr_dir = os.path.dirname(os.path.abspath(__file__))

with open(f"{__curr_dir}/defaults.yml") as defaults_fd:
  default_settings = load(defaults_fd, Loader=SafeLoader)
  defaults_fd.close()
