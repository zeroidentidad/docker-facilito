
ARG DISTRO="ubuntu:18.04"

FROM ${DISTRO}

ENV USER Zero

RUN mkdir app
RUN cd /app && touch data.txt

COPY ./src/ /app/src/
 
ADD pictures.tar.xz /com/src