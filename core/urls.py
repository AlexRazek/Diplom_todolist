from django.urls import path

from core import views

urlpatterns = [
    path("signup", views.SignupView.as_view()),
    path("login", views.LoginApiView.as_view(), name="login"),
    path("profile", views.ProfileView.as_view()),
    path("update_password", views.UpdatePasswordView.as_view()),
]