from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=50, null=False, default='Untitled')
    content = models.TextField(max_length=1000, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title