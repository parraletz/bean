from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'blog.views.PostList', name='home'),
    # url(r'^blog/', include('blog.urls')),
    

    url(r'^(?P<slug>[-\w\d]+).py','blog.views.PostDetail', name='view_post_detail'),


    url(r'^admin/', include(admin.site.urls)),
    url(r'^tracking/', include('tracking.urls')),
)
