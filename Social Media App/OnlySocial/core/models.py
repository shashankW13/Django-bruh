from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    email = models.EmailField(max_length=50, blank=True)
    profile_img = models.ImageField(upload_to='profile_images', default='blank-profile.png')
    location = models.CharField(max_length=100, blank=True)
    work = models.CharField(max_length=100, blank=True)
    relationship = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.user.username
