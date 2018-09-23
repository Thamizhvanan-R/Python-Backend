from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime
import os

# Create your models here.

def filename(instance, filename):
        respath = os.path.join('images/', instance.User.username,"profile"+datetime.now().strftime('%Y%m%d%H%M%S')+"."+filename.split('.')[-1])
        if os.path.exists(respath):
            os.remove(respath)
        return respath

class address(models.Model):
    Door = models.CharField(max_length = 50,help_text=" Door No of the house")
    Street = models.CharField(max_length = 50,help_text= " Street of the residence")
    City = models.CharField(max_length = 50,help_text="Current city")
    Pincode = models.IntegerField(help_text="zip code of the locality")

    def __str__(self):
        return self.Door+","+self.Street+","+self.City+" - "+str(self.Pincode)

class Profile(models.Model):
    User = models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
    GENDERS=(
    ('Male','Male'),
    ('Female','Female'),
    ('Others','Others'))
    Gender = models.CharField(max_length = 10,choices= GENDERS)
    Phone = models.CharField(max_length = 15,blank=True,null=True)
    Avatar = models.ImageField(upload_to= filename,blank=True,null=-True)
    Address = models.OneToOneField(address,on_delete=models.CASCADE,blank=True,null=True)
        
    def __str__(self):
        return str(str(self.User)+"\n Address :"+str(self.Address))


