from django.conf.urls import patterns, url

urlpatterns = patterns('blog.apps.content.views',
    url(r'^$',"main", name='main')
)