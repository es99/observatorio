ARG PYTHON_VERSION=3.9
ARG BASE_IMAGE_TAG=3.15

FROM python:${PYTHON_VERSION}-alpine${BASE_IMAGE_TAG} AS builder

LABEL org.opencontainers.image.created="26-05-25"
LABEL org.opencontainers.image.authors="Engels F. P. Souza - <engels.franca@gmail.com>"
LABEL org.opencontainers.image.url="https://github.com/es99/observatorio"

RUN <<EOF
apk add gcc
apk add g++
apk add libffi-dev
apk add libffi musl-dev mariadb-connector-c-dev
EOF

RUN adduser -D flasky
USER flasky
WORKDIR /home/flasky

COPY requirements requirements

RUN <<EOF
python -m venv venv
venv/bin/pip install --upgrade pip
venv/bin/pip install -r requirements/docker.txt
EOF

FROM python:${PYTHON_VERSION}-alpine${BASE_IMAGE_TAG}

ENV FLASK_APP=flasky.py
ENV FLASK_CONFIG=docker

RUN adduser -D flasky
USER flasky
WORKDIR /home/flasky

COPY --from=builder /home/flasky/venv ./venv

COPY cimov cimov
COPY migrations migrations
COPY flasky.py config.py boot.sh ./

EXPOSE 9000

ENTRYPOINT [ "./boot.sh" ]
