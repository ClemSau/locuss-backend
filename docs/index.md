# locuss-backend

[![Build Status](https://travis-ci.org/ClemSau/locuss-backend.svg?branch=master)](https://travis-ci.org/ClemSau/locuss-backend)
[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

Backend of the Locuss flashcard app. Check out the project's [documentation](http://ClemSau.github.io/locuss-backend/).

# Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)

# Initialize the project

Start the dev server for local development:

```bash
docker-compose up
```

Create a superuser to login to the admin:

```bash
docker-compose run --rm web ./manage.py createsuperuser
```
