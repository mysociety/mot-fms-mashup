from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include('mot_fms.urls', app_name='mot_fms', namespace='mot_fms')),
)
