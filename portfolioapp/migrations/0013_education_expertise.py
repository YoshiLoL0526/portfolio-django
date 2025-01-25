# Generated by Django 4.2.7 on 2024-09-12 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0012_rename_language_language_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree_title', models.CharField(max_length=200)),
                ('institution', models.CharField(max_length=200)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('education_level', models.CharField(choices=[('High School', 'High School'), ('Pre-University', 'Pre University'), ('Bachelor', 'Bachelor'), ('Master', 'Master'), ('Doctorate', 'Doctorate'), ('Diploma', 'Diploma')], default='High School', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Expertise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=200)),
                ('company_name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('project_url', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
