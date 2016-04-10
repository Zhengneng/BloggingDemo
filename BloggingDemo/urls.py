from django.conf.urls import include, url
from blog import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'blogpost', views.BlogPostViewSet)
router.register(r'users', views.UserViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
