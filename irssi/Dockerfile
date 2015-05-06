FROM fedora
MAINTAINER Kushal Das <kushaldas@gmail.com>

RUN yum -y update && yum clean all
RUN yum -y install irssi

ENV HOME /home/user
RUN useradd --create-home --home-dir $HOME user \
    && mkdir -p $HOME/.irssi \
    && chown -R user:user $HOME

ENV LANG C.UTF-8



WORKDIR $HOME
VOLUME $HOME/.irssi
VOLUME $HOME/irclogs

USER user
CMD ["irssi"]
