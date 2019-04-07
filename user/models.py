from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile_user")
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50,blank=True)
    gender = models.TextField(max_length=10)
    status = models.CharField(max_length=10,default='activated')
    types = models.CharField(max_length=10)
    likes = models.ManyToManyField(User,blank=True)

    def __str__(self):
        return str(self.user.username)

    def get_absolute_url(self):
        return reverse("user:profiledetail", kwargs={'id': self.user.id})

    def get_like_url(self):
        return reverse("appointment:like", kwargs={'id': self.user.id})

    def get_api_like_url(self):
        return reverse("appointment:like-api", kwargs={'id': self.user.id})
