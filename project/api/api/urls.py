
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from apiBeta import views


routers = routers.DefaultRouter()
routers.register(r'users', views.UserViewSet)
routers.register(r'groups', views.GroupViewSet)

# Setup automatic URL routing
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(routers.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
