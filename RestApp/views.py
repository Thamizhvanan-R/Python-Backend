from .serializers import ProfileSerializer
from .models import Profile,address
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser,\
    FileUploadParser
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer

# Create your views here.

class CreateView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,BasicAuthentication)
    parser_classes = (MultiPartParser,JSONParser,FileUploadParser)

    def get(self,request,format=None):
        try:
            us,created = Profile.objects.get_or_create(User=request.user)
            print(us)
            serializer = ProfileSerializer(us)
            return JsonResponse(serializer.data,safe=False)
        except Exception as err:
            print(err)
            return HttpResponse(status=404)
        
    def post(self,request):
        print(request.data)
        profile,created = Profile.objects.get_or_create(User = request.user)
        serializer = ProfileSerializer(profile,data= request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,safe=False)
        print(serializer.errors)
        return HttpResponse(JSONRenderer().render(serializer.errors), status=400)

#