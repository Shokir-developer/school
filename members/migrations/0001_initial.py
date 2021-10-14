# Generated by Django 3.2.6 on 2021-10-13 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Ismi')),
                ('surname', models.CharField(max_length=100, verbose_name='Familyasi')),
            ],
        ),
        migrations.CreateModel(
            name='Pupil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Ismi')),
                ('surname', models.CharField(max_length=100, verbose_name='Familyasi')),
                ('date', models.DateField(null=True)),
                ('info', models.TextField()),
                ('klass', models.IntegerField(choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8), ('9', 9)])),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.teacher')),
            ],
        ),
    ]
