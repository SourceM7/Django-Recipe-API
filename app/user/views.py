from rest_framework import generics

from user.serializers import UserSerializder


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializder
