# Generated by Django 3.2.12 on 2024-12-13 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20241212_1556'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='id',
        ),
        migrations.RemoveField(
            model_name='course',
            name='id',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='id',
        ),
        migrations.AddField(
            model_name='class',
            name='class_id',
            field=models.CharField(default=100, max_length=20, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AddField(
            model_name='course',
            name='course_id',
            field=models.CharField(default=100, max_length=20, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AddField(
            model_name='lesson',
            name='lesson_id',
            field=models.CharField(default=100, max_length=20, primary_key=True, serialize=False, unique=True),
        ),
    ]
