supervisord -c  /etc/supervisord.conf \
    && ./manage.py migrate --no-input \
    && ./runserver.py -H 0.0.0.0