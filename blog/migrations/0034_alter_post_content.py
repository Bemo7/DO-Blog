# Generated by Django 4.1.5 on 2023-01-28 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0033_alter_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(max_length=5500),
        ),
    ]
