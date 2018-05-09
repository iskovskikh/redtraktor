#!/bin/bash
POSTGRES_CONTAINER_NAME		= shop_postgres_1
POSTGRES_USER				= postgres
DB_NAME						= shop
docker exec -u $POSTGRES_USER $POSTGRES_CONTAINER_NAME psql -c 'DROP DATABASE $DB_NAME'