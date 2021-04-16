import base64

def str_to_bytes(data: str) -> bytes:
  return data.encode()

def bytes_to_str(data: bytes) -> str:
  return data.decode()

def bytes_to_base64(data: bytes) -> str:
  return bytes_to_str(
    data=base64.b64encode(data)
  )
