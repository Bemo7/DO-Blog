# Generated by Django 4.1.5 on 2023-01-27 21:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0030_alter_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(null=True, validators=[django.core.validators.MaxValueValidator(20)]),
        ),
    ]
