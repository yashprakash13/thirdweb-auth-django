from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("wallet_auth/", include("wallet_auth.urls")),
]
