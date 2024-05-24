#!/usr/bin/env bash
# exit on error
set -o errexit

echo "Installing the latest version of poetry..."

pip install --upgrade pip

pip install poetry==1.2.0

rm poetry.lock

poetry lock

python -m poetry install
python ./cms/manage.py collectstatic --no-input
python ./cms/manage.py makemigrations
python ./cms/manage.py migrate


