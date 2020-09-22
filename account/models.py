from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    TYPE = [
        ('Customer', 'Customer'),
        ('Resturant Owner', 'Resturant Owner')
    ]

    GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(choices=TYPE, max_length=50, blank=True)
    gender = models.CharField(choices=GENDER, max_length=50, blank=True)
    contact = models.CharField(max_length=50, blank=True)
    avatar = models.ImageField(
        upload_to='profiles', max_length=250, default='profiles/default.jpg')
    address = models.CharField(max_length=100, blank=True)
    bio = models.CharField(max_length=250, blank=True)
    blood_group = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return self.user.username


