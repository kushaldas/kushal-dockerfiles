FROM fedora:latest
MAINTAINER  Kushal Das


RUN dnf update -y


RUN groupadd -r fedora -g 1000 && useradd -u 1000 -r -g fedora -d /home/fedora fedora

RUN dnf install -y python3-flask python3-requests
RUN dnf install -y gcc python-pip python-devel
RUN dnf install -y libffi-devel libffi redhat-rpm-config openssl-devel
RUN pip install lektor
RUN dnf install -y rsync git python3-requests

WORKDIR /home/fedora
ENV HOME /home/fedora
RUN chown -R fedora:fedora ${HOME}

ADD newweb.py ${HOME}/newweb.py
ADD runhook.sh ${HOME}/runhook.sh
RUN chmod +x ${HOME}/runhook.sh

USER fedora
RUN mkdir -p ${HOME}/{source,output}
RUN cd source;git clone https://github.com/dgplug/lektorweb.git .

EXPOSE 5000
VOLUME ${HOME}/.ssh

CMD ["python3","newweb.py"]

