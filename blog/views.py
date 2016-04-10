from blog.models import BlogPost
from blog.serializers import BlogPostSerializer
from blog.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import permissions
from blog.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view, detail_route
from rest_framework.response import Response
from rest_framework import renderers
from rest_framework.response import Response
from rest_framework import viewsets

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        blogpost = self.get_object()
        return Response(blogpost.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

