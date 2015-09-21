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
RUN bash bootstrap.sh -i && bash requirements.sh

# Run install
RUN rm -f custom.cfg
RUN make clean install 

# Volume for data, cache, logfiles, ...
VOLUME /data
RUN mv /opt/conda/envs/birdhouse/var var.orig && ln -s /data /opt/conda/envs/birdhouse/var

# Ports used in birdhouse
EXPOSE 8090 8094 9001

# Start supervisor in foreground
ENV DAEMON_OPTS -n

# Configure hostname and user for services 
ENV HOSTNAME localhost
ENV USER nobody
RUN set -e "s/localhost/$HOSTNAME/" custom.cfg
RUN set -d "s/user = ''/user/ = $USER" custom.cfg

# Update config and start supervisor ...
CMD ["make", "update", "start"]

