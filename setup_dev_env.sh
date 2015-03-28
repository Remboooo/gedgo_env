#! /bin/bash
set -e

# Drop and re-create the database
mysql -u gedgo -e 'DROP DATABASE IF EXISTS gedgo;'
mysql -u gedgo -e 'CREATE DATABASE gedgo CHARSET utf8;'

# Initialize the database
python manage.py syncdb --noinput
python manage.py migrate

# Load development fixtures
python manage.py add_gedcom fixtures/dev.ged
export PYTHONPATH=./
export DJANGO_SETTINGS_MODULE=settings
python fixtures/add_dev_fixtures.py
