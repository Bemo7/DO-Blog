# Generated by Django 4.1.4 on 2023-01-23 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0028_comment_user_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user_pic',
            field=models.ImageField(default='default_pfp.png', upload_to=''),
        ),
    ]
