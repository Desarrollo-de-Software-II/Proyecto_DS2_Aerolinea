#!/bin/sh

# Mostrar el valor de la variable SECRET_KEY para depuración (quitar en producción)
echo "SECRET_KEY: $SECRET_KEY"

echo 'Running collecstatic...'
python manage.py collectstatic --no-input --settings=capstone.settings.production

echo 'Applying migrations...'
python manage.py migrate --settings=capstone.settings.production

echo 'Running server...'
gunicorn --env DJANGO_SETTINGS_MODULE=capstone.settings.production capstone.wsgi:application --bind 0.0.0.0:$PORT