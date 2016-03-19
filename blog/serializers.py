from rest_framework import serializers
from blog.models import BlogPost


class BlogPostSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    user_id = serializers.IntegerField()
    content = serializers.CharField()
    title = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return BlogPost.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.content = validated_data.get('content', instance.content)
        instance.title = validated_data.get('title', instance.title)
        instance.save()

        return instance