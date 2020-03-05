
ARG DISTRO="ubuntu:18.04"

FROM ${DISTRO}

RUN useradd -ms /bin/bash zero_user

RUN mkdir app
RUN cd /app && touch data.txt

COPY ./src/ /app/src/

USER zero_user

RUN cd /home/zero_user && touch data.txt