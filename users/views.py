from django.shortcuts import render
from .serializers import UserRegisterSerializer
from rest_framework import generics, permissions
from .serializers import UserProfileSerializer
from django.contrib.auth.models import User

class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer


class UserProfileView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # Return the currently logged-in user
        return self.request.user