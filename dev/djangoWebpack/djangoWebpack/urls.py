from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangoWebpack.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^hello/', include('helloWorld.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
