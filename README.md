# API

## Requirements

### Install and configure Docker

* Install docker-ce. [docker-ce](https://www.docker.com/community-edition)

* Intall docker-compose. [docker-compose](https://docs.docker.com/compose/install/)

### Set Var Environment

* Copy to `env.example` into `.env`

```sh
cp env.example .env
```

* Edit values in `.env`

```sh
nano .env
```

## BackEnd

* Build containers

```sh
docker-compose build
```

* Start container DB

```sh
docker-compose up -d postgres
```

* Apply migrations

```sh
docker-compose run --rm api python manage.py migrate
```

* Run Django Project

```sh
docker-compose up -d
```

* Open API on browser in Dev [127.0.0.1:8000](http://127.0.0.1:8000)

### Django Admin

* Create superuser

```sh
docker-compose run --rm api python manage.py createsuperuser
```

* Access to django admin [127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

### Run tests to code

* Run all the tests

```sh
docker-compose run --rm api py.test
```

### Run tests to style

* Run tests isort

```sh
docker-compose run --rm api isort -c -rc -df
```

* Run tests flake8

```sh
docker-compose run --rm api flake8
```

### Django Internationalization

* Execute this command to runs over the entire source tree of the current directory and pulls out all strings marked for translation.

```sh
docker-compose run --rm api python manage.py makemessages -l es
```

* Edit file api/locale/es/LC_MESSAGES/api.po and add a translation.

```sh
#: module/file.py:12
msgid "Hello world"
msgstr "Hola mundo"
```

* Compiles .po files to .mo files for use with builtin gettext support.

```sh
docker-compose run --rm api python manage.py compilemessages
```

### Run the project for Production

* Build

```sh
docker-compose -f docker-compose-production.yml build
```

* Initialize

```sh
docker-compose -f docker-compose-production.yml up -d postgres
docker-compose -f docker-compose-production.yml run --rm api python manage.py migrate --noinput
docker-compose -f docker-compose-production.yml run --rm api python manage.py collectstatic --noinput
docker-compose -f docker-compose-production.yml run --rm api python manage.py compilemessages
```

* Run Django server

```sh
docker-compose -f docker-compose-production.yml up -d
```

* Visit [138.197.72.19](http://138.197.72.19)
