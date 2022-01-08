FROM postgres:14.1

RUN apt-get update && apt-get install -y apt-transport-https ca-certificates gnupg curl vim

COPY ./docker/postgresql/docker-entrypoint-db.sh /

RUN chmod +x /docker-entrypoint-db.sh

ENTRYPOINT ["/docker-entrypoint-db.sh"]
