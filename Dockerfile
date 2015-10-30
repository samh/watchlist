FROM python:2-onbuild

#RUN apt-get install -y nginx
RUN pip install gunicorn
RUN SECRET_KEY=foo python manage.py migrate --noinput\
 && SECRET_KEY=foo python manage.py collectstatic --noinput
EXPOSE 8000
CMD [\
 "gunicorn", "--pythonpath", ".",\
 "--workers", "3", "-b", "0.0.0.0",\
 "watchlist.wsgi:application"]
USER daemon
