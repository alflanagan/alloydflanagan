FROM python:3.9.2-slim

RUN apt-get update

# ensure all deps for psycopg2 are installed
RUN apt-get install -y python3-psycopg2 git postgresql-client sass sudo gcc

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
