from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^blogposts/$', views.blog_post_list),
    url(r'^blogposts/(?P<pk>[0-9]+)/$', views.blog_post_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)