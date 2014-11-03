FROM ubuntu:14.04
MAINTAINER Carsten Ehbrecht <ehbrecht@dkrz.de>

# install build requirements
ADD ./bootstrap.sh /tmp/bootstrap.sh  
RUN cd /tmp && bash bootstrap.sh -i && cd -

RUN useradd -d /home/phoenix -m phoenix
ADD . /home/phoenix/src
RUN chown -R phoenix /home/phoenix/src

USER phoenix
WORKDIR /home/phoenix/src

RUN bash bootstrap.sh -u && make all

WORKDIR /home/phoenix/anaconda

EXPOSE 8090 8094 9001

#CMD bin/supervisord -n -c etc/supervisor/supervisord.conf && bin/nginx -c etc/nginx/nginx.conf -g 'daemon off;
CMD etc/init.d/supervisord start && bin/nginx -c etc/nginx/nginx.conf -g 'daemon off;'

