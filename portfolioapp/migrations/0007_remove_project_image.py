# Generated by Django 5.1 on 2024-09-06 01:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0006_project_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='image',
        ),
    ]
