FROM lsiobase/alpine:3.12
LABEL maintainer="GilbN"

WORKDIR /geoip2influx
COPY requirements.txt geoip2influx.py nginx_parser.py /geoip2influx/
RUN \
echo " ## Installing packages ## " && \
apk add --no-cache --virtual=build-dependencies \
    python3 \
    py3-pip \
    logrotate \
    libmaxminddb && \
echo " ## Installing python modules ## " && \
pip3 install --no-cache-dir -r requirements.txt
COPY root/ /
