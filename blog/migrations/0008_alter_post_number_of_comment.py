# Generated by Django 4.1.4 on 2023-01-04 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_number_of_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='number_of_comment',
            field=models.IntegerField(editable=False, null=True),
        ),
    ]
