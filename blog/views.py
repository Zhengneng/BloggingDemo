from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from blog.models import BlogPost
from blog.serializers import BlogPostSerializer


class JSONResponse(HttpResponse):

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def blog_post_list(request):
    if request.method == 'GET':
        blog_posts = BlogPost.objects.all()
        serializer = BlogPostSerializer(blog_posts, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BlogPostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)

        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def blog_post_detail(request, pk):
    try:
        blog_post = BlogPost.objects.get(pk=pk)
    except BlogPost.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = BlogPostSerializer(blog_post)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BlogPostSerializer(blog_post, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        blog_post.delete()
        return HttpResponse(status=204)