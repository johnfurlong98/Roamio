# Generated by Django 4.2.15 on 2024-08-28 15:26

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0002_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destination',
            name='image',
        ),
        migrations.AddField(
            model_name='destination',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
