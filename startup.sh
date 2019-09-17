#!/usr/bin/env bash
manage() {
  pipenv run ./manage.py "$@"
}

manage migrate
manage collectstatic --noinput
manage runserver 0.0.0.0:3000
