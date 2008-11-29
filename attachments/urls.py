from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^newattachment/(?P<content_type>\d+)/(?P<object_id>\d+)/$', 'attachments.views.new_attachment', name='attachment_new'),
    url(r'^deleteattachment/(?P<attachment_slug>[-\w]+)$', 'attachments.views.delete_attachment', name='attachment_delete'),
)