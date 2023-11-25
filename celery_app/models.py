from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserAccount(models.Model):
    User=models.OneToOneField(User,on_delete=models.CASCADE)
    otp=models.CharField(default="",max_length=20)
    full_name=models.CharField(max_length=35,blank=True,null=True)
    mobile_number=models.CharField(max_length=15,default="")
    profile_image=models.ImageField(upload_to='User/profile_image',default='User/profile_image/default.jpg',null=True)
    is_verified=models.BooleanField(default=False)
    when_add = models.DateTimeField(auto_now_add = True)
    def __str__(self):
    	return self.mobile_number
    

class Details(models.Model):
    name = models.CharField(max_length=30,blank=True,null=True)
    phone_number = models.CharField(max_length=13,blank=True,null=True)
    email = models.CharField(max_length=40,blank=True,null=True)
    message = models.TextField()
    when_add = models.DateTimeField(auto_now_add = True)
    road = models.CharField(max_length=20,null=True,blank=True)
    city = models.CharField(max_length=20,null=True,blank=True)
    state = models.CharField(max_length=20,null=True,blank=True)
    country = models.CharField(max_length=20,null=True,blank=True)
    salary = models.IntegerField(default=0)

    def __str__(self):
        return self.name