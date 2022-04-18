python manage.py migrate
gunicorn django_server.wsgi:application -p 8000 & nginx -g "daemon off;"