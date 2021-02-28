# debug and list the docker build context so that you can minimmize it
#
# usage:
#  docker build -f docker/context.Dockerfile -t test/buildcontext .
#
######################
FROM busybox

RUN mkdir /tmp/build/
# Add context to /tmp/build/
COPY . /tmp/build

CMD /bin/sh -i

