@echo off
rem Start manage.py with the local (i.e. virtualenv) python instead of the
rem system python (which is associated with py files).
set SECRET_KEY='foo'
python manage.py %*
