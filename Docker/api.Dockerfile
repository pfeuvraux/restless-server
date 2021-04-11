FROM python:3.9.2

RUN apt-get update && apt-get upgrade -y && \
    pip3 install pip --upgrade

RUN pip3 install \
    pydantic \
    fastapi \
    uvicorn && \
    \
    pip3 install git+https://github.com/pfeuvraux/restless

RUN useradd restless-server && \
    mkdir -p /var/lib/restless-server && \
    chown -R restless-server:restless-server /var/lib/restless-server && \
    usermod -d /var/lib/restless-server restless-server

WORKDIR /var/lib/restless-server


COPY ./app ./app

CMD uvicorn app.server:api --host 0.0.0.0 --port 3000
