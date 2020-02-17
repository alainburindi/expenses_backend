web: gunicorn expenses.wsgi --log-file -
release: python manage.py makemigrations --noinput && python manage.py migrate --noinput
