from django.db import models

<<<<<<< HEAD
class User(models.Model):
    DoesNotExist = models.ObjectDoesNotExist
    objects = models.Manager()
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

=======
# Create your models here.
>>>>>>> 2eda86e2da4e94185244b2ddc31d0d48c82f2255
