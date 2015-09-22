FROM birdhouse/bird-base
MAINTAINER https://github.com/bird-house

LABEL Description="Emu Web Processing Service" Vendor="Birdhouse" Version="0.2.1"

# Add application sources
ADD . /opt/birdhouse
RUN usermod --home /opt/birdhouse www-data

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
RUN mv /opt/conda/envs/birdhouse/var /data && ln -s /data /opt/conda/envs/birdhouse/var
RUN chown -R www-data /opt/birdhouse
RUN chown -R www-data /opt/conda
VOLUME /data

# Do run service as www-data
USER www-data
ENV HOME /opt/birdhouse

# Configure hostname and user for services 
ENV HOSTNAME localhost

# Ports used in birdhouse
EXPOSE 8090 8094 9001

# Start supervisor in foreground
ENV DAEMON_OPTS --nodaemon

# Update config and start supervisor ...
CMD ["make", "update-config", "start"]

