# Chapter 11: Books App

## About

- We’ve added a books model, learned how to change the URL structure, and switched to the much more secure UUID pattern.

## Instructions

- Start books app.

```
docker-compose exec web python manage.py startapp books
```

- Add books app to settings.
- Create books app model.
  - class Book(...):

```
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
```

- Add Book model to admin panel.
- Add a book in admin panel.
- Modify books admin to change what is displayed in the admin panel.
- Add books app url to project-level urls.
- Create books app url. (166)
- Create books app views.
- Create book list template.

- Modify books models to use UUID. (177)
- Update books urls to use UUID.

```
docker-compose exec web rm -r books/migrations
docker-compose down
```

Need to delete persisting postgres database which has older id fields.

```
# to see which records are there.
docker-volume ls
```

- Delete the record and migrate.

```
docker volume rm books_postgres_data
docker-compose up -d
docker-compose exec web python manage.py makemigrations books
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

- Make admin user and add three books using the admin panel.
- Create tests for books app.
