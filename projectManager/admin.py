from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from projectManager.models import *

class taskInline(admin.TabularInline):
    model = Task
    extra = 1
    
class ProjectAdmin( admin.ModelAdmin ):
    fieldsets = [
        ('Overview',         {'fields': ['title', 'description']}),
        ('Date information', {'fields': ['creation_date']}),
        ('Admin',            {'fields': ['admins']}),
        ('Status',           {'fields': ['status']}),
        ('Webiste',          {'fields': ['website']}),
    ]    
    inlines = [taskInline]
    list_display = ('title', 'creation_date')
    date_hierarchy = 'creation_date'
    search_fields = ['title']
    
class ProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'profiles'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (ProfileInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Task)
admin.site.register(Solution)

