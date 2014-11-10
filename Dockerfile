FROM ubuntu

RUN apt-get update
#RUN apt-get install -y nginx
RUN apt-get install -y python-setuptools
# Ubuntu has fairly old version of Python packages, so install from PyPI
RUN easy_install virtualenv
RUN virtualenv /venv
ADD . /app
RUN /venv/bin/pip install gunicorn -r /app/requirements.txt
RUN /venv/bin/python /app/manage.py syncdb --noinput\
 && /venv/bin/python /app/manage.py collectstatic --noinput
EXPOSE 8000
#CMD ["/venv/bin/gunicorn_django", "/app/watchlist_dj"]
CMD [\
 "/venv/bin/gunicorn", "--pythonpath", "/app",\
 "--workers", "3", "-b", "0.0.0.0",\
 "watchlist.wsgi:application"]
USER daemon
