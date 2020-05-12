# from django.shortcuts import render
from post.models import Post
from post.serializer import PostSerializer

# generics.py, mixins.py import
from rest_framework import generics
from rest_framework import mixins

# Create your views here.
#APIView의 단점 : 코드의 중복이 많아진다 (모델이 달라지더라도 ~List, ~Detail 등의 뷰의 논리 구조는 동일함)
#   -> 불필요한 코드를 줄이자! (이런 취지로 나온게 mixin)
#   -> 상속을 통해 이 문제를 해결!! 

#불필요한 코드 작성을 줄이기 위해 상속을 좀 많이 받아야 함
class PostList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    #qeuryset, serializer_class 등록하는 과정
    #상속받은 generics.GenericAPIView class에 정의되어 있는 변수
    #어떤 model을 기반으로 queryset을 설정할 것인지, 어떤 model을 기반으로 serialize 시킬 것인지 설정하는 것
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    #필요로 하는 HTTP 메소드 정의 & 한줄 짜리 return 문 있음
    #인자는 self, request 그리고 가변인자로 구성되어 있음(가변인자 -)
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs) #get 메소드는 'list'라는 메소드를 리턴. 해당 list 메소드는 'mixins.ListModelMixin'에 이미 정의되어 있는 함수

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs) #post 메소드는 'create'라는 메소드를 리턴. 해당 create 메소드는 'mixins.CreateModelMixin'에 이미 정의되어 있는 함수
    

class PostDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs) #get 요청이 들어오면 retireve라는 함수 리턴

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs) #put 요청이 들어오면 update라는 함수 리턴

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs) #delete 요청이 들어오면 destroy라는 함수 리턴
