FROM mysql:5.7

MAINTAINER Shinya Ueyama

RUN echo "[mysqld]" >> /etc/mysql/my.cnf && \
    echo "character-set-server=utf8" >> /etc/mysql/my.cnf && \
    echo "[client]" >> /etc/mysql/my.cnf && \
    echo "default-character-set=utf8" >> /etc/mysql/my.cnf

CMD ["mysqld"]
