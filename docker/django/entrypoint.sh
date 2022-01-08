#!/bin/bash

manage.py migrate

manage.py compilemessages
#manage.py collectstatic --noinput --ignore node_modules

exec "$@"

