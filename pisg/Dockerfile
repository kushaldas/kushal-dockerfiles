FROM fedora
MAINTAINER Kushal Das <kushaldas@gmail.com>

RUN yum -y update
RUN yum -y install wget perl-Data-Dumper perl-Text-Iconv
RUN yum -y install tar

RUN cd /root/ && wget http://prdownloads.sourceforge.net/pisg/pisg-0.73.tar.gz \
    && tar xzvf pisg-0.73.tar.gz


ADD pisg.conf /root/pisg.conf

ADD crontab.txt /root/crontab.txt
ADD runpisg.sh /root/runpisg.sh

RUN mkdir /output/

CMD /root/runpisg.sh

