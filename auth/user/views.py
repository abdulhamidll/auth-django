from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework import serializers

class TokenError(Exception):
    pass


class TokenBackendError(Exception):
    pass


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        print("data = super()", super().ukam())

        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data["salom"] = "salommmmmmmmmmmmmmmmmmmmmmmmmmmm"

        return data

    def salom(self):
        return "salommmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm"


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        #
        # try:
        #     serializer.is_valid(raise_exception=True)
        # except TokenError as e:
        #     print("error", e)
        serializer.is_valid(raise_exception=True)
        print("serializer", serializer.validated_data)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
