ARG PYTHON_VERSION="3.10-slim"

FROM python:${PYTHON_VERSION} AS builder

LABEL org.opencontainers.image.created="26-05-25"
LABEL org.opencontainers.image.authors="Engels F. P. Souza - <engels.franca@gmail.com>"
LABEL org.opencontainers.image.url="https://github.com/es99/observatorio"

RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    libffi-dev \
    libssl-dev

RUN useradd -m \
    -s /usr/bin/nologin flasky

USER flasky
WORKDIR /home/flasky

COPY requirements requirements

RUN <<EOF
python -m venv venv
venv/bin/pip install --upgrade pip
venv/bin/pip install -r requirements/docker.txt
EOF

FROM python:${PYTHON_VERSION}

ENV FLASK_APP=flasky.py
ENV FLASK_CONFIG=docker

RUN useradd -m \
    -s /usr/sbin/nologin flasky

USER flasky
WORKDIR /home/flasky

COPY --from=builder /home/flasky/venv ./venv

COPY cimov cimov
COPY migrations migrations
COPY flasky.py config.py boot.sh ./

EXPOSE 9000

ENTRYPOINT [ "./boot.sh" ]