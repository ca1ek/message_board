from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
        url(r'^$', views.forums, name='index'),
        url(r'^forum/(?P<forum_slug>[\w\-]+)/$', views.forum, name='forum'),
        url(r'^thread/(?P<thread_slug>[\w\-]+)/$', views.thread, name='thread'),
        url(r'^new_post/(?P<thread_slug>[\w\-]+)/$', views.new_post, name='new_post'),
        url(r'^new_post/(?P<thread_slug>[\w\-]+)/(?P<post_id>[\w\-]+)/$', views.new_post, name='quote_post')
        )