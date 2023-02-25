from django.urls import path

from .views import SignUpPageView


urlpattern = [
    path("signup/", SignUpPageView.as_view(), name="signup"),
]
