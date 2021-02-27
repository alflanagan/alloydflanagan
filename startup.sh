#!/usr/bin/env bash
manage() {
  pipenv run python ./manage.py "$@"
}

manage migrate
manage runserver 0.0.0.0:3000
