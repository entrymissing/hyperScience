from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    affiliation = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.affiliation

class Project(models.Model):
    title = models.CharField(max_length=200)
    creation_date = models.DateTimeField('date created', default = timezone.now)
    description = models.TextField()
    admins = models.ManyToManyField(User)
    status = models.CharField(max_length=20)
    website = models.URLField(blank = True)
    
    def __unicode__(self):
        return self.title
    
class Task(models.Model):
    title = models.CharField(max_length=200)
    creation_date = models.DateTimeField('date created', default = datetime.now)
    description = models.TextField()
    project = models.ForeignKey(Project)
    status = models.CharField(max_length=20)
    contributors = models.ManyToManyField(User, blank = True)

    def __unicode__(self):
        return self.title
    
class Solution(models.Model):
    title = models.CharField(max_length=200)
    task = models.ForeignKey(Task, blank = True)
    creation_date = models.DateTimeField('date created', default = datetime.now)
    description = models.TextField()
    editors = models.ManyToManyField(User, blank = True)
    status = models.CharField(max_length=20)
 
    def __unicode__(self):
        return self.title
 