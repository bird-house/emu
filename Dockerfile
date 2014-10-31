FROM ubuntu:14.04
MAINTAINER Carsten Ehbrecht <ehbrecht@dkrz.de>

RUN apt-get update

# install project requirements
ADD ./requirements.sh /tmp/requirements.sh  
RUN cd /tmp && bash requirements.sh && cd -

RUN useradd -d /home/emu -m emu
ADD . /home/emu/src
RUN chown -R emu /home/emu/src

USER emu
WORKDIR /home/emu/src

RUN bash bootstrap.sh && make all

WORKDIR /home/emu/anaconda

EXPOSE 8090 8094 9001

#CMD bin/supervisord -n -c etc/supervisor/supervisord.conf && bin/nginx -c etc/nginx/nginx.conf -g 'daemon off;
CMD etc/init.d/supervisord start && bin/nginx -c etc/nginx/nginx.conf -g 'daemon off;'

