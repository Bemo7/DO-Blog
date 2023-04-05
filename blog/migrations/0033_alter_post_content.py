# Generated by Django 4.1.5 on 2023-01-28 00:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0032_alter_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(null=True, validators=[django.core.validators.MinLengthValidator(10), django.core.validators.MaxLengthValidator(5700)]),
        ),
    ]
