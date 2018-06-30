#!/bin/sh


python3 /data/web/manage.py makemigrations
python3 /data/web/manage.py migrate
python3 /data/web/manage.py collectstatic --noinput


/usr/bin/gunicorn redtraktor.wsgi:application -w 2 --timeout 360 -b :8000