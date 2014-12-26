from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from projectManager.models import Project, Solution, Task
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def initModels(request):
    if Project.objects.filter(title='Test Project').count():
        return HttpResponse('Project already exists')
    else:
        newProject = Project(title='Test Project',
                             description='This is a test project',
                             status = 'Testing')
        newProject.save()
        newProject.admins.add(User.objects.get(username='engel'))
        newProject.save()
        
        return HttpResponse('Project created')
