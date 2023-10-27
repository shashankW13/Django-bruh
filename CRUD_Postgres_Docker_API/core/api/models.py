from django.db import models

class User(models.Model):
    DoesNotExist = models.ObjectDoesNotExist
    objects = models.Manager()
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

