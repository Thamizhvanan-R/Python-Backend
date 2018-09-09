from django.db import models
from django.conf import settings

# Create your models here.

class address(models.Model):
    Door = models.CharField(max_length = 50,help_text=" Door No of the house")
    Street = models.CharField(max_length = 50,help_text= " Street of the residence")
    City = models.CharField(max_length = 50,help_text="Current city")
    Pincode = models.IntegerField(help_text="zip code of the locality")

    def update_field(self, key, value):
     # This will raise an AttributeError if the key isn't an attribute
     # of your model
     getattr(self, key)
     setattr(self, key, value)

    def __str__(self):
        return self.Door+","+self.Street+","+self.City+" - "+str(self.Pincode)

class Profile(models.Model):
    User = models.OneToOneField(settings.AUTH_USER_MODEL,
                                       on_delete=models.CASCADE,blank=True,null=True)
    GENDERS=(
    ('Male','Male'),
    ('Female','Female'),
    ('Others','Others'))
    Gender = models.CharField(max_length = 10,choices= GENDERS)
    Phone = models.CharField(max_length = 15,blank=True,null=True)
    Avatar = models.ImageField(upload_to= "Images/",blank=True,null=-True)
    Address = models.OneToOneField(address,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return str(str(self.User)+"\n Address :"+str(self.Address))
