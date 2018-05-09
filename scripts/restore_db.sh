#!/bin/bash
cat $1 | docker.exe exec -i shop_postgres_1 psql -U postgres