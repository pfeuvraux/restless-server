FROM python:3.9.2

RUN apt-get update && apt-get upgrade -y && \
    pip3 install pip --upgrade

RUN pip3 install \
    pydantic \
    fastapi \
    uvicorn && \
    \
    pip3 install git+https://github.com/pfeuvraux/restless
