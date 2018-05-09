#!/bin/bash
source '../common.env'
docker.exe exec -t -u $DB_SERVICE redtraktor_postgres_1 pg_dumpall -f ./backup/dump_`date +%d-%m-%Y_%H_%M_%S`.sql