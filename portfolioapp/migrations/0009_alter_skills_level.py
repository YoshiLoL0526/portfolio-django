# Generated by Django 5.1 on 2024-09-06 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0008_skills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='level',
            field=models.CharField(choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced'), ('Expert', 'Expert')], default='Beginner', max_length=15),
        ),
    ]
