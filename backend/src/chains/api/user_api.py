from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response

from chains.api.utils import JSONResponse
from ..forms import NewUser


@api_view(["POST"])
def create_user(request) -> Response:
    form = NewUser(request.data)
    if form.is_valid():
        data = form.cleaned_data
        User.create_user(
            username=data.get("username"),
            email=data.get("email"),
            password=data.get("password1")
        )
        response = JSONResponse(message="Account created")
    else:
        response = JSONResponse(
            message="An error occurred while creating your account",
            error=True,
            data=form
        )
    return response.response()


@api_view(["GET"])
def authenticate_user(request):
    pass
