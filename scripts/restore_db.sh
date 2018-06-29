#!/bin/bash
source '../common.env'
source "$HOME/.bashrc"
echo $DB_USER
echo $DB_NAME
docker exec -i redtraktor_postgres_1 psql --username $DB_USER -c "CREATE DATABASE $DB_NAME OWNER $DB_USER"

cat $1 | docker exec -i redtraktor_postgres_1 psql --username $DB_USER