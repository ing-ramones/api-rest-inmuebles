# API REST INMOBILIARIA

Es un CRUD basico hecho con el framework Django y usando Postgres para la persistencia de los datos

## Requisitos

```bash
> docker / docker-compose
> git (Opcional)
> linux / windows / os
```

## Instalación

Hacer git clone

```bash
git clone -b docker https://github.com/ing-ramones/inmuebleapp.git
```

Ejecutar los comandos docker-compose en un terminal en la raiz del proyecto:

```bash
# 1- Build Docker-Compose
$ docker-compose -f docker-compose.yml build

# 2- Up Docker-Compose
$ docker-compose up
```

En otro terminal en la raiz del proyecto ejecutar:

```bash
# 3- Run Makemigrations
$ docker-compose -f docker-compose.yml run --rm web python manage.py makemigrations

# 4- Run migrate
$ docker-compose -f docker-compose.yml run --rm web python manage.py migrate

# 5- Run createsuperusere
$ docker-compose -f docker-compose.yml run --rm web python manage.py createsuperuser
# Completar los datos que solicita y listo
```

Test

```bash
# 1- Run pytest
$ docker-compose -f docker-compose.yml run --rm web pytest -v

# 2- Run coverage
$ docker-compose -f docker-compose.yml run --rm web coverage

# >>> Coverage HTML written to dir htmlcov <<<
```

## Uso

```bash
# Entrar al administrador (Con el usuario que creaste en los pasos previos)
http://127.0.0.1:8000/admin

# Swagger
http://127.0.0.1:8000/swagger

# Redoc
http://127.0.0.1:8000/redoc
```

## Fuentes principales en las que me basé para el desarrollo

```bash
# Documentación oficial de Django
https://docs.djangoproject.com/en/3.1/

# Django rest framework
https://www.django-rest-framework.org/

# Classy Class-Based Views
http://ccbv.co.uk/
```

## License

[BSD](https://choosealicense.com/bsd)
