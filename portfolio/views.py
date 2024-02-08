from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
import markdown

from .models import Project, ProfessionalExperience, SkillCategory, Skill


def portfolio(request):
    projects = Project.objects.all()
    professional_experiences = ProfessionalExperience.objects.all()
    skill_categories = SkillCategory.objects.all()
    skills = Skill.objects.all()
    return render(request, 'portfolio.html', {'projects': projects, 'professional_experiences': professional_experiences,
                                              'skill_categories': skill_categories, 'skills': skills})


def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    project.content = markdown.markdown(project.content)
    return render(request, 'project_detail.html', {'project': project})


def experience_detail(request, experience_id):
    experience = get_object_or_404(ProfessionalExperience, id=experience_id)
    experience.content = markdown.markdown(experience.content)
    return render(request, 'experience_detail.html', {'experience': experience})
