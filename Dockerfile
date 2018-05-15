# vim:set ft=dockerfile:
FROM continuumio/miniconda3
MAINTAINER https://github.com/bird-house/emu
LABEL Description="Emu: Demo PyWPS" Vendor="Birdhouse" Version="0.6"

# Update conda
RUN conda update -n base conda

# Copy WPS project
COPY . /opt/emu

WORKDIR /opt/emu

# Create conda environment
RUN conda env update -f environment.yml

# Install WPS
RUN /opt/conda/envs/emu/bin/python setup.py install

# Start WPS service on port 5000 on 0.0.0.0
EXPOSE 5000
ENTRYPOINT ["/opt/conda/envs/emu/bin/emu", "-a"]
CMD ["-c", "/opt/emu/emu/default.cfg"]

# docker build -t emu .
# docker run -p 5000:5000 emu
# http://localhost:5000/wps?request=GetCapabilities&service=WPS
# http://localhost:5000/wps?request=DescribeProcess&service=WPS&identifier=all&version=1.0.0
