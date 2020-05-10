# from django.shortcuts import render
# 위에 꺼 안쓰나봄..!

# 데이터 처리 대상
from post.models import Post
from post.serializer import PostSerializer

# status에 따라 직접 Response를 처리할 것
from django.http import Http404

# APIView를 상속받은 CBV 는 Response와 status를 import하여 status를 활용하여 직접 Response를 만들어 줌!!
from rest_framework.response import Response
from rest_framework import status

# APIView를 상속받은 CBV
from rest_framework.views import APIView

# 굳이 PostDetail 클래스의 get_object 함수 안만들고 그냥 있는거 써도 됨
# -> 그냥 있는거 가져다가 쓰는거랑 내가 정의한 함수 쓰는거랑은 퍼포먼스 적으로 동인한가?? 그럼 어떤걸 쓰는게 더 좋은 코드일까????
from django.shortcuts import get_object_or_404


# Create your views here.

'''
APIView를 상속받은 CBV 사용하는 방법(쓰는 이유/의의)
class ~~~(APIVeiw):
    def <내가 필요로 하는 HTTP Method>:
        Http Method로 어떻게 처리할 지 직접 정의하기
        (Resopnse와 status를 사용하여)
'''
class PostList(APIView):
    def get(self, request): #APIView를 상속받아 CBV를 사용할 때는 내부에서 사용할 HTTP 메소드의 이름으로 메소드(메소드의 이름)를 정의해야 함
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True) #다수의 객체/query set를 Serializer 로 보내줄때는 뒤에 "many=True" 인자를 넣어야 함!
        return Response(serializer.data) #serializer에 있는 data를 그냥 Response로 보내준다

    def post(self, request): #새 Post를 작성할때 내용을 다 작성하고 제출버튼을 누르면 호출되는 것이 이 post 메소드
        serializer = PostSerializer(data=request.data) #그러므로 이 serializer에는 내가 request를 보낸 data가 직렬화가 되야한다
        if serializer.is_valid(): #serializer를 유효성 검사를 하고 
            serializer.save() #문제가 없으면 저장!
            return Response(serializer.data, status=status.HTTP_201_CREATED) #문제없이 저장이 되었으면, serializer.data와 status를 같이 보내준다
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) #유효성 검사 쪽에서 문제가 생기면 "HTTP_400_BAD_REQUEST"를 status에 담아 error와 함께 Response를 전송
        '''질문! 그러면 Response의 첫번째 인자가 data에 해당하는데 어떤 의미의? data를 의미하는지 궁금'''

#여기서 PostDetail 치면 자동완성되던데 왜 자동완성이 되는거지...?
class PostDetail(APIView):
    #get_object_or_404를 직접 구현한 것
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):
        post = self.get_object(pk) #해당 pk에 해당하는 object를 가지고 와서 
        # post = get_object_or_404(Post, pk)
        serializer = PostSerializer(post) #해당 object 직렬화 한다음
        return Response(serializer.data) #Response에 담아 리턴. 만약에 해당 pk에 해당하는 객체가 없으면 404가 리턴됨

    
    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self, request, pk, format=None):
        post = get_object(pk) #pk에 해당하는 post 가지고 와서 
        post.delete() #지우고 나서
        return Response(status=status.HTTP_204_NO_CONTENT) #지웠으니 이제 해당하는 content 없다는 의미로 HTTP_204_NO_CONTENT 보내줌
