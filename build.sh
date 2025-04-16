#!/usr/bin/env bash
pip install -r requirements.txt
playwright install
python manage.py migrate