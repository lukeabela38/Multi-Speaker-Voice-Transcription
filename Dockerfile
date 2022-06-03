FROM ubuntu:22.04

RUN apt-get -y update && apt-get install -y \
    python3-dev \
    python3-pip \
python3-setuptools

RUN apt install -y git
RUN apt install -y ffmpeg

WORKDIR /workspace

COPY requirements.txt requirements.txt
RUN python3 -m pip install -r requirements.txt
COPY src .