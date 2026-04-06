from django.urls import include, path
from rest_framework import routers

from .api import create_user, authenticate_user

router = routers.DefaultRouter()
# router.register(r"create_user", create_user)
# router.register(r"user_auth", authenticate_user)

urlpatterns = [
    path("create_user/", create_user),
]
