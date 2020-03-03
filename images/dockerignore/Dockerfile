
ARG DISTRO="ubuntu:18.04"

FROM ${DISTRO}

RUN mkdir app
RUN cd /app && touch data.txt

COPY ./src/ /app/src/
