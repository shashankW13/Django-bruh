# Generated by Django 4.2.6 on 2023-11-23 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_comment_user_email_alter_comment_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user_email',
            field=models.EmailField(max_length=254),
        ),
    ]
