# URLS FOR LOGIN

from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^success$', views.success), # success page
    url(r'^process$', views.process_users), # register process
    url(r'^login$', views.login), # login process
    url(r'^clear$', views.clear), # logout and clear sessions

]