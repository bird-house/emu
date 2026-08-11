# vim:set ft=dockerfile:
FROM condaforge/miniforge3
ARG DEBIAN_FRONTEND=noninteractive
ENV PIP_ROOT_USER_ACTION=ignore
LABEL org.opencontainers.image.authors="Birdhouse"
LABEL org.opencontainers.image.created="2026-08-11T14:39:02Z"
LABEL org.opencontainers.image.source="https://github.com/bird-house/emu"
LABEL org.opencontainers.image.title="EmuWPS"
LABEL org.opencontainers.image.vendor="Birdhouse"
LABEL org.opencontainers.image.version="1.0.0-dev.0"
LABEL Description="Emu WPS"

# Set the working directory to /code
WORKDIR /code

# Create conda environment
COPY environment-docker.yml .
RUN conda env create -n emu -f environment-docker.yml && \
    conda install -n emu gunicorn && \
    conda clean --all --yes

# Add the project conda environment to the path
ENV PATH="/opt/conda/envs/emu/bin:$PATH"

# Copy WPS project
COPY . /code

# Install WPS project
RUN conda run -n emu pip install . --no-deps

# Start WPS service on port 5000 on 0.0.0.0
EXPOSE 5001
CMD ["gunicorn", "--bind=0.0.0.0:5000", "emu.wsgi:application"]
# docker build -t birdhouse/emu .
# docker run -p 5000:5000 birdhouse/emu
# http://localhost:5000/wps?request=GetCapabilities&service=WPS
# http://localhost:5000/wps?request=DescribeProcess&service=WPS&identifier=all&version=1.0.0
