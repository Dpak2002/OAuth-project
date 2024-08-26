from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView
)
from rest_framework.permissions import IsAuthenticated
from oauth2_provider.contrib.rest_framework import TokenHasScope, TokenHasReadWriteScope
from .serializers import UserSerializer

class CreateUserAPI(CreateAPIView):
    permission_classes = [IsAuthenticated, TokenHasReadWriteScope]
    serializer_class = UserSerializer


class ListUserAPI(ListAPIView):
    permission_classes = [IsAuthenticated, TokenHasReadWriteScope]
    serializer_class = UserSerializer
    queryset = User.objects.all()

class DetailUserAPI(RetrieveAPIView):
    permisssion_classes = [IsAuthenticated, TokenHasReadWriteScope]
    serializer_class = UserSerializer
    queryset = User.objects.all()