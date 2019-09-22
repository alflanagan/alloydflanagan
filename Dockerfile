FROM python

RUN apt-get update

# ensure all deps for psycopg2 are installed
RUN apt-get install -y python3-psycopg2 git postgresql-client sass

RUN python3 -m pip install pipenv

RUN adduser --gecos '' --disabled-password alloydflanagan 

RUN mkdir -p /usr/src/app/alloydflanagan && chown alloydflanagan:alloydflanagan /usr/src/app/alloydflanagan

WORKDIR /usr/src/app/alloydflanagan

COPY Pipfile Pipfile

COPY Pipfile.lock Pipfile.lock

RUN chown alloydflanagan:alloydflanagan Pipfile Pipfile.lock

USER alloydflanagan

RUN pipenv sync

USER root

COPY . .

RUN chown -R alloydflanagan:alloydflanagan .

USER alloydflanagan
