from rest_framework.authentication import BasicAuthentication,TokenAuthentication, SessionAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from userpost.models import UserPost
from rest_framework import viewsets
from userpost.serializer import UserSerializer
from rest_framework.filters import SearchFilter

class UserPostViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    queryset = UserPost.objects.all()
    serializer_class = UserSerializer

    filter_backends = [SearchFilter]
    # 무엇을 기반으로
    search_fields = ('title', 'body', )
    # 어떤 컬럼을 기반으로 -> tuple
    
    def get_queryset(self):
        qs = super().get_queryset() # usper class(UserPostViewSet)의 queryset을 가져온다

        # 사용자 지정 방식으로 filter
        # qs = qs.filter(author__id=1)
        # qs.exclude로도 가능

        # 지금 만약 로그인 -> 유저 글만
        if self.request.user.is_authenticated:
            qs = qs.filter(author=self.request.user)

        # 로그인 안되어 있다면 -> 비어있는 쿼리셋 return
        else:
            qs  = qs.none()
        return qs

    # 현재 그 유저로 내용 저장
    # create 함수 호출해줌 -> perform_create
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)