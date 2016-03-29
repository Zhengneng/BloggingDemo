from rest_framework import serializers
from blog.models import BlogPost
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    blogpost = serializers.PrimaryKeyRelatedField(many=True, queryset=BlogPost.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'blogpost')

class BlogPostSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = BlogPost
        fields = ('created', 'user_id', 'content', 'title', 'owner')


