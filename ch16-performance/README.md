# Chapter 16: Performance

## About

## Instructions

- Install django-debug-toolbar.
- Update settings to add debug toolbar.
- Add urlpattern to add debug toolbar.

- Use the toolbar and click SQL in one of the books. (book details)

  - Observe the “N+1 Queries problem.” (241)
  - We want to update this to prefetch_related all the reviews for each author in one go.
    - Update book app views, BookDetailView.

- Update book models in class Meta to add index field.

```
docker-compose exec web python manage.py makemigrations books
docker-compose exec web python manage.py migrate
```


- Update settings to add caching.
