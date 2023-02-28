# Chapter 14: Permissions

## About

Permissions and groups are a highly subjective topic that can vary widely from project to project. The basic approach, however, remains the same and mimic what we’ve covered here: start by restricting access and only gradually loosed it to users as needed. In our case we restricted access to only logged in users and from there added additional permissions around what groups of logged in users could view.

## Instructions

- Update books app views to require login to view book list and book details pages.

  - Import LoginRequiredMixin

- Update books app models to add a speical status so that an author can read all books.
  - class Meta: ...

```
docker-compose exec web python manage.py makemigrations books
docker-compose exec web python manage.py migrate
```

- Create a special user to give special permissions to in the admin panel.

  - Go to User Permissions and select 'books | book | Can read all books.'
  - Apply custom permission in books app views. (214)
    - Import PermissionRequiredMixin.

- LoginRequiredMixin and PermissionRequiredMixin must come before DetailView.

```
class BookDetailView( LoginRequiredMixin,
        PermissionRequiredMixin,  # new
        DetailView):
```
