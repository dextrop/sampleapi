#!/bin/bash
pip install -r requirements.txt
python manage.py makemigrations src
python manage.py migrate