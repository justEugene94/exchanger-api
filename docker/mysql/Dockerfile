FROM mysql:5.7

COPY mysql.cnf /etc/mysql/conf.d/mysql.cnf

ENTRYPOINT ["docker-entrypoint.sh"]

EXPOSE 3306

RUN usermod -u 1000 www-data