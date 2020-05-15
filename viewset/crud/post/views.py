# from django.shortcuts import render

from post.models import Post
from post.serializer import PostSerializer

from rest_framework import viewsets

from rest_framework import renderers
from rest_framework.decorators import action
from django.http import HttpResponse

# Create your views here.
'''
ViewSet에는 4가지가 존재
    1)class Viewset(ViewSetMixins, views.APIView)
    2)class GenericViewSet(ViewSetMixins, generics.GenericalAPIView)
    3)class ReadOnlyModeViewSet(mixins.RetrieveModeMixins,
                                mixins.ListModelMixins,
                                GenericViewSet)
    4)class ModelViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.ListModelMixin,
                        GenericViewSet)

https://github.com/encode/django-rest-framework/blob/master/rest_framework/viewsets.py

4개의 class가 있는데 내부를 보면, pass와 상속이 다임. 
    => 상속받은 N개의 인자 그냥 묶어 준 것!

    3)ReadOnlyModelViewSet
    """
    A viewset that provides default `list()` and `retrieve()` actions.
    """
    => mixins.RetrieveModeMixins -> retrieve() 이게 전부 : 특정, 객체 레코드 가져다 주는 역할
       mixins.ListModelMixins -> list() 이게 전부 : 객체, 레코드 목록 가져다 주는 역할
        ∴ read only를 수행해준다

    이전에는 UserList, UserDetail 같이 listview, detailview 따로 구현했음
     ~> but 이젠, ReadOnlyModelViewSet을 상속받은 UserViewSet으로 한번에 구현할 수 있다.

    queryset과 serializer_class만 등록해주면 읽기 기능만 수행하는 뷰 만들 수 있다


    4)ModelViewSet
    이 내용은 아래 코드로 설명함



'''

'''
https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/
'''



# class PostViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
 

    # #ListView, DetailView 랑 CRUD 아닌 custom ?? 요청을 처리하는 방법
    # permission_classes = [permissions.IsAuthenicatedOrReadOnly, IsOwnerOrReadOnly]
    # '''permission_classes : Action을 수행할 수 있는 권한을 설정하는 부분'''
    # '''permissions.IsAuthenticatedOrReadOnly : 권한을 권한이 있는 사람으로부터 요청(인증된 요청에 대해서만 권한을 줄거임) 그렇지 않은 인증 요청에 대해서는 읽기 권한만 줄 것이다'''
    # '''IsOwnerOrReadOnly : 소유자 인 사람, 그렇지 않은 사람에게는 읽기 권한만 준다'''

    #"@action" + "함수들" : 장식자(decorator)
    @action(detail=True, renderer_classes = [renderers.StaticHTMLRenderer]) #@action(method=['post'], ...) 이런식으로 POST 방식으로 사용할 수도 있음
    def highlight(self, request, *args, **kwargs):
        return HttpResponse("얍얍 커피먹으러가자!")

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    # viewset에서 CRUD 아닌 다른 logic 어떻게 구현...?(나만의 custom API)
    #   우리가 임의 대로 view 설계한다 (≈ drf apiview에서 Response, status Import해서)
    #   => 그래서 위에 action, Response import


    # ∴ action decorater 쓰고 그 아래에 CRUD가 아닌 동작 or 논리를 담은 custom API를 작성
    #   => 여러분만의 CRUD가 아닌 custom API가 만들어짐


    #renderer_classes 인자는
    #   우리가 만들 custom API의 Response 객체를 어떻게 렌더링 시킬지
    #
    #   ex) JSONRenderer - default
    #   ex) BrowsableAPIRenderer - default
    #   +a ex) StaticHTMLRenderer, TemplateHTMLRenderer
    # 
    # custom API의 default Method 는 "GET"!
    # (만약 다른 Method를 수행하고 싶으면, action의 format 인자를 지정하면 됨!)