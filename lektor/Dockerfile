FROM fedora:latest
MAINTAINER  Kushal Das

RUN dnf install -y python-flask python-requests
RUN dnf install -y gcc python-pip python-devel
RUN dnf install -y libffi-devel libffi redhat-rpm-config openssl-devel
RUN pip install lektor
RUN dnf install -y rsync git
ADD newweb.py /newweb.py
ADD runhook.sh /runhook.sh
RUN chmod +x /runhook.sh
RUN mkdir /{source,output}
RUN cd source;git clone https://github.com/dgplug/lektorweb.git .

EXPOSE 5000

CMD ["python","newweb.py"]
