FROM ubuntu

ENV USER Zero

RUN mkdir app
RUN cd /app && touch data.txt

COPY ./src/ /app/src/
 
ADD pictures.tar.xz /com/src