# Generated by Django 4.1.4 on 2023-01-10 20:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_remove_about_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='position',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)]),
        ),
    ]
