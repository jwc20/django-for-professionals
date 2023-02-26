# Chapter 8: Advanced User Registration

- Install django-allauth.

```
docker-compose down
docker-compose up -d --build
```

- Add django.contrib.sites in settings.
- Add django-allauth to INSTALLED_APPS in settings.
- Update AUTHENTICATION_BACKENDS in settings.
- Add EMAIL_BACKENDS in settings.
- Add LOGIN_REDIRECT_URL in settings.
- Add ACCOUNT_LOGOUT_REDIRECT_URL in settings.

```
docker-compose exec web python3 manage.py migrate
```

- Update project-level urls to use allauth accounts urls.

```
mkdir templates/account
mv templates/registration/login.html templates/account/login.html
mv templates/registration/signup.html templates/account/signup.html
```

- Update base.html to use url from allauth.
- Add staticfiles.
- Add option to remember logging in.
- Create logout template.
- Update settings to require typing password once when signing up.
- Added django.contrib.sites to installed apps.
- Updated settings to require email when logging in and not username.
- Updated signup tests for allauth.

```
docker-compose exec web python manage.py test
```
