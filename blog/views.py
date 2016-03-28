from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog.models import BlogPost
from blog.serializers import BlogPostSerializer

@api_view(['GET', 'POST'])
def blog_post_list(request, format=None):
    if request.method == 'GET':
        blog_posts = BlogPost.objects.all()
        print 'erers'
        serializer = BlogPostSerializer(blog_posts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BlogPostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def blog_post_detail(request, pk, format=None):
    try:
        blog_post = BlogPost.objects.get(pk=pk)
    except BlogPost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BlogPostSerializer(blog_post)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BlogPostSerializer(blog_post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        blog_post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)