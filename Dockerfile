FROM ubuntu:latest
LABEL authors="dima"

ENTRYPOINT ["top", "-b"]