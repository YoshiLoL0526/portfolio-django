# Generated by Django 5.1 on 2024-09-03 23:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0004_tag_remove_project_tags_project_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='image',
        ),
    ]
