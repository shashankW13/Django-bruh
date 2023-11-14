from django.db import models
from django.utils.text import slugify
from django.core.validators import MinLengthValidator

class Tag(models.Model):
    caption = models.CharField(max_length=20)

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()

class Post(models.Model):
    title = models.CharField(max_length=50, default='Untitled', null=False)
    excerpt = models.CharField(max_length=200, null=False)
    image_name = models.CharField(max_length=20, blank=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(default='',
                            unique=True,
                            blank=False,
                            null=False)
    content = models.TextField(validators=[MinLengthValidator(50)], null=False, blank=False)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name='posts')
    tags = models.ManyToManyField(Tag)