#! /bin/bash
set -e

# Build dependencies
virtualenv virtualenv
virtualenv/bin/pip install --upgrade setuptools==1.4 pip==1.5 wheel
virtualenv/bin/pip install --allow-external PIL --allow-unverified PIL -r gedgo/reqs.pip

# Drop and re-create the database
mysql -u root -e 'DROP DATABASE IF EXISTS gedgo;'
mysql -u root -e 'CREATE DATABASE gedgo CHARSET utf8;'


## TODO: Import SQL dump from fixtures and apply migrations.

# Initialize the database
virtualenv/bin/python manage.py syncdb --noinput
virtualenv/bin/python manage.py migrate

# Load development fixtures
virtualenv/bin/python manage.py add_gedcom fixtures/dev.ged
export PYTHONPATH=./
export DJANGO_SETTINGS_MODULE=settings
virtualenv/bin/python fixtures/add_dev_fixtures.py
