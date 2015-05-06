FROM fedora
MAINTAINER Kushal Das <kushaldas@gmail.com>

RUN yum -y update && yum clean all
RUN yum -y install irssi

ENV HOME /home/kdas
RUN useradd --create-home --home-dir $HOME kdas \
    && mkdir -p $HOME/.irssi \
    && mkdir -p $HOME/irclogs \
    && chown -R kdas:kdas $HOME

ENV LANG C.UTF-8



WORKDIR $HOME
VOLUME $HOME/.irssi
VOLUME $HOME/irclogs

USER kdas
CMD ["irssi"]
