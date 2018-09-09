from .serializers import ProfileSerializer
from .models import Profile,address
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.template.context_processors import request
from django.http import HttpResponse, JsonResponse

# Create your views here.

class CreateView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,BasicAuthentication)

    def get(self,request,format=None):
        try:
            us = Profile.objects.get(User=request.user)
            serializer = ProfileSerializer(us)
            return JsonResponse(serializer.data,safe=False)
        except :
            return HttpResponse(status=404)

    def post(self,request):
        try:

            print(request.data)
            Profile1, created = Profile.objects.get_or_create(User = request.user)
            Profile1.Gender = request.data['detail']['Gender']
            Profile1.Phone = request.data['detail']['Phone']

            if(not Profile1.Address):
                Profile1.Address = address()
            Address = Profile1.Address
            for key, value in request.data['detail']['Address'].items():
                Address.update_field(key, value)
            Address.save()
            Profile1.Address = Address

            user = Profile1.User
            for key, value in request.data['user'].items():
                setattr(user,key,value)
            user.save()
            Profile1.User = user
            Profile1.save()
            print("*********\n")
            print(Profile1)
            print("*********\n")
            return HttpResponse(status=200)
        except(ex):
            print(ex)
            return HttpResponse(status=500)

