from django.db import models
from django.db.models.query_utils import PathInfo
from django.urls import reverse
from django.contrib.auth.models import User
import uuid
from django.conf import settings


class GitUser(models.Model):
    username = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.username


class Repository(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=40, null=True, blank=True)
    url = models.URLField()
    owner = models.ForeignKey(GitUser, related_name="repositories", on_delete=models.CASCADE)


    def __str__(self):
        return self.name + " - " + self.owner.username
