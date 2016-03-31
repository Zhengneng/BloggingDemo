from django.conf.urls import include, url
from blog import views

urlpatterns = [
    # url(r'^', include(router.urls)),
    url(r'^', include('blog.urls')),
    # url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
