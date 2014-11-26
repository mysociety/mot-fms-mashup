from django.conf.urls import patterns, include, url
from django.contrib import admin

from mot_fms.views import PostcodeListView, PostcodeDetailView, VehicleMakeListView, VehicleMakeDetailView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mot_fms_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', PostcodeListView.as_view(), name='postcode-list'),
    url(r'^postcode/(?P<pk>[-_\w]+)/$', PostcodeDetailView.as_view(), name='postcode-detail'),

    url(r'^vehicle/$', VehicleMakeListView.as_view(), name='vehicle-make-list'),
    url(r'^vehicle/(?P<pk>\d+)/$', VehicleMakeDetailView.as_view(), name='vehicle-make-detail'),
)
