# Generated by Django 5.1 on 2024-09-06 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0009_alter_skills_level'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Skills',
            new_name='Skill',
        ),
    ]
