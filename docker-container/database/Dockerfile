FROM postgres:9.6.20

RUN export DEBIAN_FRONTEND=noninteractive \
 && apt-get update \
 && apt-get install -y curl \
 && apt-get install wget \
 && apt-get install -y lsb-release \
 && apt-get install -y apt-utils \
 && apt-get clean all \
 && apt-get update \ 
 && apt-get install -y postgresql-9.6-postgis-scripts
