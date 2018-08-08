from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer
from .models import user

# Create your views here.

class CreateView(generics.ListCreateAPIView):
    queryset = user.objects.all()
    serializer_class = UserSerializer

    def perform_create(self , serializer):
        serializer.save()
