"""
* This scripts logs in the API in order to
* retrieve a token for further tests
"""

from argparse import ArgumentParser
import srp
from base64 import b64encode
import requests
import json

def _parse_args():

  parser = ArgumentParser()
  parser.add_argument('--host', required=False, default='127.0.0.1')
  parser.add_argument('--port', required=False, default=3000)
  parser.add_argument('--username', required=True)
  parser.add_argument('--password', required=True)

  return parser.parse_args()

if __name__ == "__main__":

  cli_args = _parse_args()

  salt, vkey = srp.create_salted_verification_key(
    cli_args.username,
    cli_args.password
  )

  salt_b = b64encode(salt).decode('utf-8')
  vkey_b = b64encode(vkey).decode('utf-8')
  payload = {
    "username": cli_args.username,
    "srp_salt": salt_b,
    "srp_verifier": vkey_b
  }
  headers = {
    "content-type": "application/json"
  }
  res = requests.post(
    url=f"http://{cli_args.host}:{cli_args.port}/auth/register",
    data=json.dumps(payload),
    headers=headers
  )

  print('---- RESPONSE ----')
  print(res.text)

  print('---- STATUS CODE ----')
  print(res.status_code)
