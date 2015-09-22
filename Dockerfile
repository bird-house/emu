FROM birdhouse/bird-base
MAINTAINER https://github.com/bird-house

LABEL Description="Emu Web Processing Service" Vendor="Birdhouse" Version="0.2.1"

# Set current home
ENV HOME /root

# Add application sources
ADD . /opt/birdhouse

# cd into application
WORKDIR /opt/birdhouse

# Install system dependencies
RUN bash bootstrap.sh -i && bash requirements.sh

# Set conda enviroment
ENV ANACONDA_HOME /opt/conda
ENV CONDA_ENVS_DIR /opt/conda/envs

# Run install
RUN make clean install 

# Volume for data, cache, logfiles, ...
RUN mv $CONDA_ENVS_DIR/birdhouse/var /data && ln -s /data $CONDA_ENVS_DIR/birdhouse/var
RUN chown -R www-data $CONDA_ENVS_DIR/birdhouse
VOLUME /data

# Configure hostname and user for services 
ENV HOSTNAME localhost

# Ports used in birdhouse
EXPOSE 8090 8094 9001

# Start supervisor in foreground
ENV DAEMON_OPTS --nodaemon --user www-data

# Update config and start supervisor ...
CMD ["make", "update-config", "start"]

