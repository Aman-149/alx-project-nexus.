#!/bin/bash
# Build script for Render/Railway deployment
set -o errexit

pip install -r requirements.txt
python manage.py migrate --no-input
python manage.py collectstatic --no-input --clear
