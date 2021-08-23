from django.contrib import admin
from .models import GitUser, Repository

admin.site.register(GitUser)
admin.site.register(Repository)