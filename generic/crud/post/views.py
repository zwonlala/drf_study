# from django.shortcuts import render
from post.models import Post
from post.serializer import PostSerializer
from rest_framework import generics #geneics는 이전에 한 mixins의 중복되는 코드를 생략할 수 있는 더 간단한 방식.

#이전 mixins 코드
'''
class PostList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs) 

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs) 
'''

# Create your views here.
class PostList(generics.ListCreateAPIView): #상속받은 generics의 ListCreteAPIView는 위의 mixins 코드에서 구현한 get, post 함수가 이미 구현되어 있는 클래스.(get, post 함수에서 실행하는 "list" 함수와 "create"함수가 이 클래스 이름을 정의)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


'''
class PostDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs) 

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs) 

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs) 
'''
class PostDetail(generics.RetrieveUpdateDestroyAPIView): #상속받은 generics의 RetrieveUpdateDestroyAPIView는 위의 mixins 코드에서 구현한 get, put, delete 함수가 이미 구현되어 있는 클래스. (get, put, delete 함수에서 실행하는 "retrieve", "update", "destroy" 함수가 이 클래스 이름을 정의)
    queryset = Post.objects.all()
    serializer_class = PostSerializer