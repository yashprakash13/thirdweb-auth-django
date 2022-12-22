from django.urls import path
from .views import login, logout, authenticate

urlpatterns = [
    path("login", login),
    path("logout", logout),
    path("authenticate", authenticate),
]
