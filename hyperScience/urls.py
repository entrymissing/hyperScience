from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^init', 'projectManager.views.initModels', name='init'),
    url(r'^admin/', include(admin.site.urls)),
)
