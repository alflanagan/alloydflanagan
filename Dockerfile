FROM python

RUN apt-get update

# ensure all deps for psycopg2 are installed
RUN apt-get install -y python3-psycopg2 git postgresql-client

RUN python3 -m pip install pipenv

RUN adduser --gecos '' --disabled-password alloydflanagan 

RUN mkdir -p /usr/src/app/alloydflanagan && chown alloydflanagan:alloydflanagan /usr/src/app/alloydflanagan

USER alloydflanagan

WORKDIR /usr/src/app/alloydflanagan

COPY . .

RUN pipenv sync
