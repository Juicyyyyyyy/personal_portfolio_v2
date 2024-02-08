from django.db import models
from django.contrib.postgres.fields import ArrayField


class ProfessionalExperience(models.Model):
    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=200)
    company_url = models.URLField(max_length=200)
    short_description = models.CharField(max_length=300, null=True, blank=True)
    content = models.TextField()
    thumbnail_img = models.ImageField(null=True, blank=True, upload_to="images/")
    languages_used = ArrayField(models.CharField(max_length=100))

    def __str(self):
        return f"{self.company_name}"


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    short_description = models.CharField(max_length=300, null=True, blank=True)
    content = models.TextField()
    thumbnail_img = models.ImageField(null=True, blank=True, upload_to="images/")
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    languages_used = ArrayField(models.CharField(max_length=100))
    url = models.URLField(max_length=200)

    def __str(self):
        return f"{self.name}"


class SkillCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    order = models.IntegerField(unique=True)

    def __str(self):
        return f"{self.name}"


class Skill(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    svg_icon = models.TextField()
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE)

    def __str(self):
        return f"{self.name}"
