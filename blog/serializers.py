from rest_framework import serializers
from blog.models import BlogPost
from django.contrib.auth.models import User


class BlogPostSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='blogpost-highlight', format='html')


    class Meta:
        model = BlogPost
        fields = ('created', 'url', 'user_id', 'content', 'title', 'owner', 'highlight')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    blogpost = serializers.HyperlinkedRelatedField(many=True, view_name='blogpost-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'blogpost')
