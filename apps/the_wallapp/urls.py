# URLS FOR WALL APP

from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^quotes$', views.index), # quote page
    url(r'^message$', views.message), # process quotes
    url(r'^delete_message/(?P<id>\d+)', views.delete_message), # process delete quotes
    url(r'^account/(?P<id>\d+)$', views.account), # account page
    url(r'^account/(?P<id>\d+)/edit$', views.edit), # edit account process
    url(r'^post/(?P<id>\d+)$', views.posted), # account page
    url(r'^like_message/(?P<message_id>\d+)$', views.like_message),
]