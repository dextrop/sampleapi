#!/bin/bash
pip3 install -r requirements.txt
python3 manage.py makemigrations src
python3 manage.py migrate