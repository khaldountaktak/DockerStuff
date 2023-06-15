FROM haproxytech/haproxy-alpine:2.7
EXPOSE 5555

RUN sh -c "apk add openrc"

COPY haproxyORIGINAL.cfg /usr/local/etc/haproxy/haproxy.cfg
