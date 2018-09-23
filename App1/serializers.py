from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile,address
from drf_extra_fields.fields import Base64ImageField
from DjangoAppEnv.Lib.functools import partial
from rest_framework.renderers import JSONRenderer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = address
        fields = ('Door','Street','City','Pincode')

class ProfileSerializer(serializers.ModelSerializer):

    User = UserSerializer(many=False,partial=True)
    Address = AddressSerializer(many=False)
    Avatar=Base64ImageField(required=True)
    class Meta:
        model = Profile
        fields = ('User','Gender','Avatar','Phone','Address')
        depth = 1
        
    def create(self, validated_data):
        print("Create called")
        return serializers.ModelSerializer.create(self, validated_data)
    
    def update(self, instance, validated_data):
        print("IN Update")
        print(instance)
        self._updateProfile(instance, validated_data)
        return instance
        
    def _updateProfile(self,profile,data):
        profile.Gender = data['Gender']
        profile.Phone = data['Phone']
        profile.Avatar = data['Avatar']
        profile.User = self._updateUser(profile.User,data['User'])
        profile.Address = self._updateAddress(profile.Address,data['Address'])
        profile.save()
        return profile
        
    def _updateUser(self,User,data):
     #   User.username = data['username']
        User.first_name = data['first_name']
        User.last_name = data['last_name']
        User.save()
        return User
    
    def _updateAddress(self,Address,data):
        Address.Door = data['Door']
        Address.Street = data['Street']
        Address.City = data['City']
        Address.Pincode = data['Pincode']
        Address.save()
        return Address;
        
        
   
        