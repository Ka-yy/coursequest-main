# Generated by Django 3.2.12 on 2024-12-15 18:03

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_course_course_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='class',
            options={'ordering': ['order'], 'verbose_name_plural': 'Classes'},
        ),
        migrations.AlterModelOptions(
            name='lesson',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='class',
            name='order',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='lesson',
            name='duration',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lesson',
            name='order',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='class',
            name='class_id',
            field=models.CharField(default=main.models.generate_unique_id, max_length=20, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_id',
            field=models.CharField(default=main.models.generate_unique_id, max_length=20, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='lesson_id',
            field=models.CharField(default=main.models.generate_unique_id, max_length=20, primary_key=True, serialize=False, unique=True),
        ),
    ]
