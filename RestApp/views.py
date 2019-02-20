from .serializers import ProfileSerializer
from .models import Profile,address
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication, BasicAuthentication,\
    SessionAuthentication
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser,\
    FileUploadParser
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from django.http.response import Http404
from rest_framework.generics import ListCreateAPIView
from RestApp.models import Post
from RestApp.serializers import PostSerializer

# Create your views here.

class ProfileView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (SessionAuthentication, TokenAuthentication,BasicAuthentication)
    parser_classes = (MultiPartParser,JSONParser,FileUploadParser)
    
    def get_object(self, user):
        try:
            profile= Profile.objects.get(User=user)
            return profile
        except:
            raise Http404

    def get(self,request,format=None):
        profile = self.get_object(request.user)
        serializer = ProfileSerializer(profile)
        return JsonResponse(serializer.data,safe=False)
        
    def post(self,request):
        profile,created= Profile.objects.get_or_create(User=request.user)
        serializer = ProfileSerializer(profile,data= request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,safe=False)
        return JsonResponse(serializer.errors, status=400)

class postlist(ListCreateAPIView):
    
    permission_classes = (IsAuthenticated,)
    authentication_classes = (SessionAuthentication, TokenAuthentication,BasicAuthentication)
    parser_classes = (MultiPartParser,JSONParser,FileUploadParser)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def filter_queryset(self, queryset):
        queryset = queryset.filter(owner = self.request.user)
        return queryset
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
  
    #===========================================================================
    # def get(self,request,format=None):
    #     posts = Post.objects.filter(owner=request.user)
    #     serializer = PostSerializer(posts,many=True)
    #     return JsonResponse(serializer.data,safe = False)
    # 
    # def post(self,request,format=None):
    #     serializer = PostSerializer(data = request.data)
    #     
    #===========================================================================
    

#