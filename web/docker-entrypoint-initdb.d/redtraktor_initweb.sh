#!/bin/sh


python3 /data/web/manage.py makemigrations
python3 /data/web/manage.py migrate
python3 /data/web/manage.py collectstatic
