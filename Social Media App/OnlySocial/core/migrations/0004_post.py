# Generated by Django 4.2.4 on 2023-10-04 12:46

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_profile_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='post_images')),
                ('caption', models.TextField(max_length=50)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('number_of_likes', models.IntegerField(default=0)),
            ],
        ),
    ]