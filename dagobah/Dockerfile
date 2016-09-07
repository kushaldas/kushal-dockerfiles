FROM fedora:latest

MAINTAINER Kushal Das <kushaldas@gmail.com>

RUN groupadd -g 1000 go && useradd -d /home/go -g 1000 go
RUN dnf install tar wget git vim -y && dnf clean all

ENV GOPATH=/home/go/gocode/
ENV GOROOT=/home/go/go/
ENV PATH=/home/go/go/bin:/home/go/gocode/bin:${PATH}


RUN dnf install mongodb-server -y && dnf clean all

USER go
WORKDIR /home/go

RUN wget https://storage.googleapis.com/golang/go1.7.linux-amd64.tar.gz && \
    tar -xzvf go1.7.linux-amd64.tar.gz

RUN go get github.com/GeertJohan/go.rice && go get github.com/GeertJohan/go.rice/rice

RUN go get github.com/spf13/dagobah; exit 0
RUN sed -i  's/viper.Marshal/viper.Unmarshal/' ${GOPATH}/src/github.com/spf13/dagobah/commands/fetch.go

RUN cd ${GOPATH}/src/github.com/spf13/dagobah/commands && \
    rice embed-go && cd .. && go build && mv dagobah ${GOPATH}/bin/

VOLUME /home/go/.dagobah
RUN mkdir -p /home/go/db/logs

ADD ./start.sh /usr/bin/
EXPOSE 1138

CMD ["/usr/bin/start.sh"]
