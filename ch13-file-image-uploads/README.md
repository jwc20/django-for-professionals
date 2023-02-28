# Chatper 13: File/Image Uploads

## About

- This chapter demonstrated how to add user files to a project. In practice it is straightforward, but the additional layer of security concerns makes it an area worthy of focus at scale.

## Instructions

- Install Pillow.
- Add MEDIA_URL and MEDIA_ROOT to settings.

```
mkdir media
mkdir media/covers
```

- Update project-level urls to include files locally. (197)
- Add covers property to book model. (199)

```
docker-compose exec web python manage.py makemigrations books
```

- Update book detail template to show cover image.
