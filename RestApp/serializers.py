from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile,address
from drf_extra_fields.fields import Base64ImageField
from _overlapped import NULL
from RestApp.models import Post

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

    def update(self, instance, validated_data):
        try:
            if (not instance.Address):
                instance.Address = address()
            self._update(instance, validated_data)
            return instance
        except AttributeError as err:
            print(err)
            raise serializers.ValidationError(err)

    def _update(self,model,data):
        for key,val in data.items():
            if(isinstance(val,dict)):
                innermodel = getattr(model, key)
                self.updatefield(model, key,(self._update(innermodel,val)))
            else:
                self.updatefield(model, key, val)
        model.save()
        return model

    def updatefield(self,model,key,value):
        field = getattr(model,key,NULL)
        if field != NULL:
            setattr(model,key,value)
        else:
            raise AttributeError


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source = 'owner.username')
    class Meta:
        model = Post
        fields = '__all__'







