# from django.shortcuts import render
# 위에 꺼 안쓰나봄..!

# 데이터 처리 대상
from post.models import Post
from post.serializer import PostSerializer

# status에 따라 직접 Response를 처리할 것
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status

# APIView를 상속받은 CBV
from rest_framework.views import APIView

# 굳이 PostDetail 클래스의 get_object 함수 안만들고 그냥 있는거 써도 됨
# -> 그냥 있는거 가져다가 쓰는거랑 내가 정의한 함수 쓰는거랑은 퍼포먼스 적으로 동인한가?? 그럼 어떤걸 쓰는게 더 좋은 코드일까????
from django.shortcuts import get_object_or_404


# Create your views here.
class PostList(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#여기서 PostDetail 치면 자동완성되던데 왜 자동완성이 되는거지...?
class PostDetail(APIView):

    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        # post = get_object_or_404(Post, pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    
    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self, request, pk, format=None):
        post = get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
