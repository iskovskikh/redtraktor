#!/bin/bash
source '../common.env'
source "$HOME/.bashrc"
docker exec -i redtraktor_postgres_1 psql -U postgres -c "DROP DATABASE $DB_NAME"