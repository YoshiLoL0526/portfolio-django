from django.contrib import admin
from .models import Project, Tag, Skill, Language, Education, Expertise, Information

# Register your models here.
admin.site.register(Project)
admin.site.register(Tag)
admin.site.register(Skill)
admin.site.register(Language)
admin.site.register(Education)
admin.site.register(Expertise)
admin.site.register(Information)
