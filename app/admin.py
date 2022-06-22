# app/admin.py
from django.contrib import admin
from .models import Article, Recruiter, Employee, Apply

admin.site.register(Article)
admin.site.register(Recruiter)
admin.site.register(Employee)
admin.site.register(Apply)