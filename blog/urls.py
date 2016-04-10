from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from views import BlogPostViewSet, UserViewSet, api_root
from rest_framework import renderers


blogpost_list = BlogPostViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

blogpost_detail = BlogPostViewSet.as_view({
    'get': 'retrive',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

blogpost_highlight = BlogPostViewSet.as_view({
    'get': 'highlight'

}, renderer_class=[renderers.StaticHTMLRenderer])

user_list = UserViewSet.as_view({
    'get': 'list'
})

user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = format_suffix_patterns([
    url(r'^$', api_root),
    url(r'^blogposts/$', blogpost_list, name='blogpost-list'),
    url(r'^blogposts/(?P<pk>[0-9]+)/$', blogpost_detail, name='blogpost-detail'),
    url(r'^blogposts/(?P<pk>[0-9]+)/highlight/$', blogpost_highlight, name='blogpost-highlight'),
    url(r'^users/$', user_list, name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail')
])

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]