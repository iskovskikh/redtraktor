#!/bin/sh


mkdir -p /data/web/test
echo 1234
echo 1234
python3 /data/web/manage.py makemigrations
python3 /data/web/manage.py migrate
python3 /data/web/manage.py collectstatic