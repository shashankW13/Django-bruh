from collections.abc import Iterable
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

class Country(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=2)

    class Meta:
        verbose_name_plural = 'Countries'

    def __str__(self) -> str:
        return f'{self.name}'
    

class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.street}, {self.postal_code}, {self.city}'
    
    class Meta:
        verbose_name_plural = 'Address'

class Author(models.Model):

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self) -> str:
        return self.full_name()

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    author = models.ForeignKey(Author, 
                               on_delete=models.CASCADE, 
                               null=True, related_name='books')
    is_bestselling = models.BooleanField(default=False) 
    slug = models.SlugField(default='', 
                            blank=True, 
                            null=False, 
                            db_index=True)
    published_countries = models.ManyToManyField(Country, null=False)

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])

    def __str__(self) -> str:
        return f'{self.title} ({self.rating})'