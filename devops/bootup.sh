#!/bin/sh

python manage.py collectstatic --no-input
python manage.py migrate --no-input
python manage.py import-iam feeds/iam.data.json
python manage.py import-utilities feeds/utilities.data.json

python manage.py runserver 0.0.0.0:8000