# Generated by Django 3.2.12 on 2024-12-15 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20241213_0834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_id',
            field=models.CharField(default='<functio', max_length=20, primary_key=True, serialize=False, unique=True),
        ),
    ]