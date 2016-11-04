from django.conf.urls import url
import views
from .import views

urlpatterns = [
    url(r'^blog/$', views.post_list),
    url(r'^(?P<id>\d+)/$', views.post_details,name='post_detail'),
    url(r'^post/new/$', views.new_post, name='new_post'),
    url(r'^blog/(?P<id>\d+)/edit$',views.edit_post),
]