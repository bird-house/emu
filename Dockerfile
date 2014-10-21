FROM ubuntu:14.04
MAINTAINER Carsten Ehbrecht <ehbrecht@dkrz.de>

RUN apt-get update && apt-get install -y git wget
WORKDIR /tmp
RUN wget https://raw.githubusercontent.com/bird-house/emu/master/requirements.sh
RUN bash requirements.sh
RUN useradd -d /home/phoenix -m phoenix
USER phoenix
RUN git clone https://github.com/bird-house/emu.git
RUN cd emu && bash install.sh && cd -
WORKDIR /home/phoenix/anaconda
EXPOSE 8094 9001
