# Generated by Django 3.2.12 on 2024-12-12 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='course',
            old_name='School',
            new_name='school',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='Summary',
            new_name='summary',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='Title',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='school',
            name='image',
        ),
        migrations.RemoveField(
            model_name='school',
            name='location',
        ),
        migrations.RemoveField(
            model_name='school',
            name='year_established',
        ),
        migrations.AddField(
            model_name='course',
            name='outline',
            field=models.TextField(default='This is the course outline '),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('class_obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='main.class')),
            ],
        ),
        migrations.AddField(
            model_name='class',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classes', to='main.course'),
        ),
    ]
