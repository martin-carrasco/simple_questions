#!/bin/bash
set -eu

date=`date`
echo "Startup at $date"

exec env POSTGRES_PASSWORD=$APPDB_PWD POSTGRES_USER=$APPDB_USER POSTGRES_DB=$APPDB_NAME docker-entrypoint.sh postgres -N $APPDB_MAX_CONNECTIONS 

exit
