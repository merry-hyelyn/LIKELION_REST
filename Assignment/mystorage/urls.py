from rest_framework.routers import DefaultRouter
from django.urls import path, include
from mystorage import views

routers = DefaultRouter()
routers.register('essay', views.PostViewSet)
routers.register('album', views.ImgViewSet)
routers.register('files', views.FileViewSet)

urlpatterns = [
    path('', include(routers.urls)),
]