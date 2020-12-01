FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y apt-utils \
 && apt-get install -y curl && apt-get install -y iputils-ping \
 && apt-get install -y gdal-bin

RUN mkdir /server

WORKDIR /server/

COPY . /server/

RUN pip install --upgrade pip

RUN cd /server/

RUN pip install -r /server/requirements.txt
