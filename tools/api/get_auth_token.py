"""
* This scripts logs in the API in order to
* retrieve a token for further tests
"""

from argparse import ArgumentParser
import srp

def _parse_args():

  parser = ArgumentParser()
  parser.add_argument('--host', required=False, default='127.0.0.1')
  parser.add_argument('--port', required=False, default=3000)
  parser.add_argument('--username', required=True)
  parser.add_argument('--password', required=True)

  return parser.parse_args()

def challenge():
  pass

if __name__ == "__main__":

  cli_args = _parse_args()

