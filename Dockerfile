FROM ubuntu:14.04
MAINTAINER Emu WPS Application

# Add application sources
ADD . /opt/birdhouse

# Set conda enviroment
ENV ANACONDA_HOME /opt/anaconda
ENV CONDA_ENVS_DIR /opt/conda_envs

# cd into application
WORKDIR /opt/birdhouse

# Install system dependencies
RUN bash bootstrap.sh -i && bash requirements.sh

# Update makefile and run install
RUN bash bootstrap.sh -u && make clean install 

# cd into conda birdhouse environment
WORKDIR /opt/conda_envs/birdhouse

# volume for variable data
VOLUME /birdhouse
RUN mv var var.orig && ln -s /birdhouse var

# all currently used ports in birdhouse
EXPOSE 8090 8094

CMD ["bin/supervisord", "-n", "-c", "etc/supervisor/supervisord.conf"]

