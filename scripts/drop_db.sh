#!/bin/bash
source '../common.env'
source "$HOME/.bashrc"
docker exec -i redtraktor_postgres_1 psql -U $DB_USER -c "DROP DATABASE $DB_NAME"