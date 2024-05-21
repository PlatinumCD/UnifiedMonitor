FROM ubuntu:22.04

RUN apt update -y && \
    apt install -y vim python3 python3-pip tree

RUN pip3 install openai

RUN mkdir -p /opt/cbin && mkdir -p /root/.openai

ADD ./.secrets/ai /opt/cbin/ai
ADD ./.secrets/master.key /root/.openai/master.key

ENV PATH="${PATH}:/opt/cbin"

WORKDIR /local
