# Generated by Django 4.1.5 on 2023-02-01 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0046_alter_staff_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user_pic',
            field=models.ImageField(default='default_pfp.jpg', upload_to=''),
        ),
    ]
