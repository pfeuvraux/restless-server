# FIXME: do some better tooling here

docker-compose up -d scylladb

sleep 30

docker-compose up --build app
