# Generated by Django 4.1.4 on 2023-01-04 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_comment_comment_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='number_of_comment',
            field=models.IntegerField(null=True),
        ),
    ]
