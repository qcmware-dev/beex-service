from django.contrib import admin
from django.urls import path
from django.urls import include
from rest_framework import routers
from beex import views

router = routers.DefaultRouter()
router.register(r'auth', views.UserViewSet)
router.register(r'users', views.BeexUserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('login/', include('beex.mviews.login')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]