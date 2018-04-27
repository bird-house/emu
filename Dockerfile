# vim:set ft=dockerfile:
FROM alpine:latest
MAINTAINER https://github.com/bird-house/emu

RUN apk add --no-cache \
	git \
	gcc \
	bash \
	openssh \
	musl-dev  \
	python3 \
	python3-dev \
	libxml2-dev  \
	libxslt-dev \
	linux-headers

RUN git clone https://github.com/bird-house/emu.git

WORKDIR /emu
RUN pip3 install -r requirements.txt
RUN python3 setup.py install

EXPOSE 5000
ENTRYPOINT ["/usr/bin/python3", "emu","-a"]

#docker build -t emu .
#docker run -p 5000:5000 emu
#http://localhost:5000/wps?request=GetCapabilities&service=WPS
#http://localhost:5000/wps?request=DescribeProcess&service=WPS&identifier=all&version=1.0.0
