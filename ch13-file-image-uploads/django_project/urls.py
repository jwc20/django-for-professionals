from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("accounts/", include("django.contrib.auth.urls")),
    # path("accounts/", include("accounts.urls")),
    path("accounts/", include("allauth.urls")),
    path("", include("pages.urls")),
    path("books/", include("books.urls")),
]
