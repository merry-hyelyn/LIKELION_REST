from rest_framework.pagination import PageNumberPagination 
from .models import Post
from rest_framework import viewsets
from .serializer import PostSerializer
from post.pagination import MyPagination

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('id')
    serializer_class = PostSerializer
    pagination_class = MyPagination
