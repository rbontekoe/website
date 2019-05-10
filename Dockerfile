FROM python

RUN apt-get -q update && \
    apt-get -qy install \
	wget curl

RUN pip3 install flask flask-wtf flask-bootstrap flask-nav gunicorn

WORKDIR ./web

COPY . /web
