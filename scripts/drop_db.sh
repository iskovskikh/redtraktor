#!/bin/bash
source '../common.env'
docker exec -i redtraktor_postgres_1 psql -c "DROP DATABASE $DB_NAME"