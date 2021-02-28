FROM python:3.9.2-slim

RUN apt-get update && apt-get -y install gnupg2 wget sudo lsb-release

# and... Postrgres client for this image defaults to version 11, add repos so we can
# get 13
# Create the file repository configuration:
RUN sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

# Import the repository signing key:
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -

# Update the package lists:
RUN apt-get update
# Install the latest version of PostgreSQL.
# If you want a specific version, use 'postgresql-12' or similar instead of 'postgresql':
RUN apt-get -y install postgresql-client-13 python3-psycopg2 git sass sudo gcc

RUN python3 -m pip install pipenv

RUN adduser --gecos '' --disabled-password alloydflanagan

RUN echo 'alloydflanagan      ALL    = NOPASSWD:ALL' >> /etc/sudoers

RUN mkdir -p /usr/src/app/alloydflanagan && chown alloydflanagan:alloydflanagan /usr/src/app/alloydflanagan

WORKDIR /usr/src/app/alloydflanagan

COPY --chown=alloydflanagan:alloydflanagan Pipfile Pipfile

COPY Pipfile.lock Pipfile.lock

RUN chown alloydflanagan:alloydflanagan Pipfile Pipfile.lock

USER alloydflanagan

RUN pipenv sync

COPY --chown=alloydflanagan:alloydflanagan . .

RUN pipenv run python manage.py collectstatic --no-input

CMD "pipenv run python manage.py runserver 0.0.0.0:3000"
