from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from django.contrib.auth.models import User

class UserCreate(APIView):
    """
    Creates the user.
    """


    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        print(request.data);
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response("Cannot be created")
