# Generated by Django 3.2.6 on 2021-10-14 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_auto_20211013_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='pupil',
            name='images',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
