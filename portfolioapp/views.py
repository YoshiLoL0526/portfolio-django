from django.shortcuts import render
from django.db.models import Case, When, Value, IntegerField
from .models import Project, Skill, Language, Expertise, Education


def home(request):
    # Obtener todos los proyectos
    projects = Project.objects.prefetch_related('tags').all().order_by('-id')[:3]

    # Definir el orden de los niveles de habilidad
    skill_order = Case(
        When(level='Expert', then=Value(4)),
        When(level='Advanced', then=Value(3)),
        When(level='Intermediate', then=Value(2)),
        When(level='Beginner', then=Value(1)),
        output_field=IntegerField(),
    )

    # Definir el orden de los niveles de idioma
    language_order = Case(
        When(level='Native', then=Value(7)),
        When(level='C2', then=Value(6)),
        When(level='C1', then=Value(5)),
        When(level='B2', then=Value(4)),
        When(level='B1', then=Value(3)),
        When(level='A2', then=Value(2)),
        When(level='A1', then=Value(1)),
        output_field=IntegerField(),
    )

    skills = Skill.objects.all().annotate(order=skill_order).order_by('-order')[:6]
    languages = Language.objects.all().annotate(order=language_order).order_by('-order')[:5]
    expertises = Expertise.objects.all().order_by('-end_date')[:3]
    educations = Education.objects.all().order_by('-end_date')[:3]

    context = {
        'projects': projects,
        'skills': skills,
        'languages': languages,
        'expertises': expertises,
        'educations': educations
    }
    return render(request, 'home.html', context)


def all_projects(request):
    query = request.GET.get('q')
    tag_filter = request.GET.get('tag')

    projects = Project.objects.all()

    if query:
        projects = projects.filter(title__icontains=query)

    if tag_filter:
        projects = projects.filter(tags__name__icontains=tag_filter)

    return render(request, 'all_projects.html', {'projects': projects})
