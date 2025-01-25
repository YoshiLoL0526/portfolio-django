from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Project(models.Model):
    tags = models.ManyToManyField(Tag, related_name='projects')
    title = models.CharField(max_length=200)
    description = models.TextField()
    # image = models.ImageField(upload_to='img/', blank=True)
    link = models.URLField(blank=True)

    def __str__(self):
        return f"{self.title}"


class Skill(models.Model):
    class Levels(models.TextChoices):
        BEGINNER = 'Beginner'
        INTERMEDIATE = 'Intermediate'
        ADVANCED = 'Advanced'
        EXPERT = 'Expert'

    name = models.CharField(max_length=200)
    level = models.CharField(max_length=15, choices=Levels.choices, default=Levels.BEGINNER)

    def __str__(self):
        return f"{self.name} level {self.level}"


class Language(models.Model):
    class Levels(models.TextChoices):
        A1 = 'A1'
        A2 = 'A2'
        B1 = 'B1'
        B2 = 'B2'
        C1 = 'C1'
        C2 = 'C2'
        NATIVE = 'Native'

    name = models.CharField(max_length=200)
    level = models.CharField(max_length=15, choices=Levels.choices, default=Levels.A1)

    def __str__(self):
        return f"{self.name} level {self.level}"


class Education(models.Model):
    class Levels(models.TextChoices):
        HIGH_SCHOOL = 'High School'
        PRE_UNIVERSITY = 'Pre-University'
        BACHELOR = 'Bachelor'
        MASTER = 'Master'
        DOCTORATE = 'Doctorate'
        DIPLOMA = 'Diploma'

    degree_title = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    education_level = models.CharField(max_length=50, choices=Levels.choices, default=Levels.HIGH_SCHOOL)

    def __str__(self):
        return f"{self.degree_title} at {self.institution}"


class Expertise(models.Model):
    job_title = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    project_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"


class Information(models.Model):
    TYPE_CHOICES = [
        ('contact', 'Contact'),
        ('working_hours', 'Working Hours'),
        ('client', 'Client'),
        ('coffee', 'Coffee'),
    ]

    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    key = models.CharField(max_length=100)
    value = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.type} - {self.key}"
