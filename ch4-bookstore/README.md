# Chapter 4: Bookstore Project

## Instructions

- start venv and activate
- Install django and psycopg2-binary
- Start project and runserver to check
- Create requirements
- Deactivate venv
- Create necessary docker files
  - Dockerfile
  - docker-compose.yml
  - .dockerignore
- `docker-compose up -d --build`
- Update DATABASE in django settings
- `docker-compose exec web python3 manage.py startapp accounts`
- Create model

  - Import AbstractUser and
  - class CustomUser(AbstractUser)

- Add accounts app to to settings
- Add AUTH_USER_MODEL to settings
- Migrate in docker container
- Create custom user forms

  - Import get_user_model, UserCreationForm, UserChangeForm
  - class CustomUserCreationForm(...): ...
  - class CUstomUserChangeForm(...): ...

- Update admin,py

  - Import get_user_model, UserAdmin, CustomUserCreationForm, CUstomUserChangeForm
  - class CustomUserAdmin(...):

- Create superuser

- Create tests for creating custom user and superuser
  - Import get_user_model
