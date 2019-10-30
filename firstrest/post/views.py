from django.http import HttpResponse
from .models import Post
from .serializer import PostSerializer
from rest_framework import response
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework import renderers

# class PostViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # GET 방식으로 method
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    # 그냥 얍을 띄우는 custom api
    def highlight(self, request, *args, **kwargs):
        return HttpResponse("얍")