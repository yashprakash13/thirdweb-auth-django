import os
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from thirdweb import ThirdwebSDK
from thirdweb.types import LoginPayload
from datetime import datetime, timedelta


@api_view(["POST"])
def login(request):
    if request.method == "POST":
        private_key = os.environ.get("ADMIN_PRIVATE_KEY")
        if not private_key:
            print("Missing ADMIN_PRIVATE_KEY environment variable")
            return Response(
                "Admin private key not set", status=status.HTTP_400_BAD_REQUEST
            )
        sdk = ThirdwebSDK.from_private_key(private_key, "mumbai")
        payload = LoginPayload.from_json(request.json["payload"])

        # Generate an access token with the SDK using the signed payload
        domain = "yourwebsitedomain.com"
        token = sdk.auth.generate_auth_token(domain, payload)

        response = HttpResponse("Works")
        response.set_cookie(
            "access_token",
            token,
            path="/",
            httponly=True,
            secure=True,
            samesite="strict",
        )
        return Response({"Success": response}, status=status.HTTP_200_OK)


@api_view(["POST"])
def logout(request):
    if request.method == "POST":
        response = HttpResponse("Works")
        response.set_cookie(
            "access_token", "none", expires=datetime.utcnow() + timedelta(seconds=5)
        )
        return Response({"Success": response}, status=status.HTTP_200_OK)


@api_view(["POST"])
def authenticate(request):
    if request.method == "POST":
        private_key = os.environ.get("ADMIN_PRIVATE_KEY")
        if not private_key:
            print("Missing ADMIN_PRIVATE_KEY environment variable")
            return Response(
                "Admin private key not set", status=status.HTTP_400_BAD_REQUEST
            )

        sdk = ThirdwebSDK.from_private_key(private_key, "mumbai")

        # Get access token off cookies
        token = request.cookies.get("access_token")
        if not token:
            return Response("Unauthorized", status=status.HTTP_401_UNAUTHORIZED)

        domain = "yourwebsitedomain.com"
        try:
            address = sdk.auth.authenticate(domain, token)
        except:
            return Response("Unauthorized", status=status.HTTP_401_UNAUTHORIZED)

        return JsonResponse(address, status=status.HTTP_200_OK)
