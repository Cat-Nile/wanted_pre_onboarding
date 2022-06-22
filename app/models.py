# app/models.py
from django.db import models

class Recruiter(models.Model):
    name = models.CharField(max_length=60)
    nation = models.CharField(max_length=30)
    location = models.CharField(max_length=128)
    def __str__(self):
        return f"{ self.name }"

class Article(models.Model):
    author = models.ForeignKey(Recruiter,
                               on_delete=models.CASCADE, related_name='articles')
    # author = models.CharField(max_length=50)
    position = models.CharField(max_length=120)
    description = models.TextField()
    bonus = models.CharField(max_length=50)
    skill = models.CharField(max_length=128)
    def __str__(self):
        return f"{self.author} {self.position}"

class Employee(models.Model):
    username = models.CharField(max_length=40)
    def __str__(self):
        return f"{ self.username }"

class Apply(models.Model):
    applicant = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='applies')
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='receives')
    def __str__(self):
        return f"{ self.applicant } { self.article_id }"

