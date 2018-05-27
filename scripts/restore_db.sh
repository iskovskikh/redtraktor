#!/bin/bash
source '../common.env'
source "$HOME/.bashrc"
docker exec -i redtraktor_postgres_1 psql -U $DB_USER -c "CREATE DATABASE $DB_NAME OWNER $DB_USER"

cat $1 | docker exec -i redtraktor_postgres_1 psql -U $DB_USER