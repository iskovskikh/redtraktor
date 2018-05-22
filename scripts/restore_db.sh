#!/bin/bash
source '../common.env'
cat $1 | docker exec -i redtraktor_postgres_1 psql -U postgres