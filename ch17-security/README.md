# Chapter 17: Security

## About

## Instructions

- Use `docker-compose exec web python -Wa manage.py test` to check for update.

- Use `docker-compose exec web python manage.py check --deploy`

- Copy the contents of the docker-compose.yml file over into docker-compose-prod.yml.

```
docker-compose down
docker-compose -f docker-compose-prod.yml up -d
```

- Set DJANGO_DEBUG to False to not allow debug toolbar.

```
docker-compose down
docker-compose -f docker-compose-prod.yml up -d
```
