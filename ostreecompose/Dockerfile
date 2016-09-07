FROM fedora:latest
MAINTAINER Kushal Das <kushaldas@gmail.com>

RUN echo "fastestmirror=true" >> /etc/dnf/dnf.conf
RUN dnf update -y
RUN dnf install -y git rpm-ostree rpm-ostree-toolbox polipo docker fuse fuse-libs python-pip gnupg patch
ENV GITURL https://github.com/kushaldas/puiterwijk-Atomic.git
ENV CONFIGDIR /srv/rpm-ostree/config
RUN mkdir -p ${CONFIGDIR}
RUN git clone ${GITURL} ${CONFIGDIR}

VOLUME /mnt

ENTRYPOINT ["/srv/rpm-ostree/config/kdas-build.sh"]
