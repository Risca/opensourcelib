FROM docker.zenterio.lan/zenterio/pythontest.u14

RUN \
apt-get update && \
apt-get --yes -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" install zenterio-zk2 firefox
