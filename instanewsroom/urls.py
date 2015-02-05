from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'instanewsroom.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^listen/', 'listener.views.listen'),

    url(r'^admin/', include(admin.site.urls)),
)
