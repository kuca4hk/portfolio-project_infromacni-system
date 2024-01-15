#!/bin/sh

#set -ex

python manage.py collectstatic --noinput &
python manage.py migrate

#python manage.py runserver 0.0.0.0:8000
gunicorn --bind :8000 --workers 3 main.wsgi:application
