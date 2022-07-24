#!/bin/sh

python manage.py migrate --no-input
python manage.py collectstatic --no-input

gunicorn ipdc.wsgi:application --bind 0.0.0.0:8000 --timeout 9000