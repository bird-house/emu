FROM continuumio/miniconda
MAINTAINER Emu WPS Application

# Add application sources
ADD . /opt/birdhouse

# Set conda enviroment
ENV ANACONDA_HOME /opt/conda
ENV CONDA_ENVS_DIR /opt/conda/envs

# cd into application
WORKDIR /opt/birdhouse

# Install system dependencies
RUN apt-get update && apt-get install -y sudo
RUN bash bootstrap.sh -i && bash requirements.sh

# Update makefile and run install
RUN make clean install 

# Volume for variable data
VOLUME /birdhouse
RUN mv /opt/conda/envs/birdhouse/var var.orig && ln -s /birdhouse /opt/conda/envs/birdhouse/var

# Custom config
RUN cp custom.cfg.example /custom.cfg
RUN rm -f custom.cfg && ln -s /custom.cfg .

# all currently used ports in birdhouse
EXPOSE 8090 8094

CMD ["make", "update", "start"]

