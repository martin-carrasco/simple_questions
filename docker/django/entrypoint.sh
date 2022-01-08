#!/bin/bash

manage.py migrate

manage.py compilemessages
manage.py collectstatic --noinput --ignore node_modules

manage.py compress

exec "$@"

