from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^', include('qa.urls')),
    url(r'^admin/', admin.site.urls),
]
"""
#2 from urls.py import test
urlpatterns = patterns('',
       #2 url(r'</d+>$', test, name='test')
    #1 url(r'</d+>$', 'qa.views.test', name='test')
    url(r'^admin/', include(admin.site.urls)),
)
"""