
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from accounts import urls as accUrls
#api
from rest_framework import routers
from tasks.views import TasksViewSet
from accounts.views import ProfileViewSet

router = routers.DefaultRouter()
router.register(r'tasks', TasksViewSet)
router.register(r'profile', ProfileViewSet)

urlpatterns = [
    url(
    regex=r'^media/(?P<path>.*)$',
    view = serve,
    kwargs={'document_root':settings.MEDIA_ROOT}
    ),
    path('admin/', admin.site.urls),
    #api
    url(r'^api/', include(router.urls)),
    url(r'^api/users/', include(accUrls, namespace='api-urls')),
    url(r'^rest-auth/', include('rest_auth.urls')),


]
