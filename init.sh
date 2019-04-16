#!/bin/bash

docker-compose up -d db

echo "Esperando a Postgres..."

sleep 10

docker cp moni-db.dump $(docker-compose ps -q db):moni-db.dump

docker exec -i $(docker-compose ps -q db) psql -U moni < moni-db.dump

docker-compose up -d web
