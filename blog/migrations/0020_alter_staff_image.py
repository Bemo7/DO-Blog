# Generated by Django 4.1.4 on 2023-01-10 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_alter_staff_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='image',
            field=models.ImageField(upload_to='staffs'),
        ),
    ]
