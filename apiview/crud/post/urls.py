from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from post import views

# Default Router 사용 X => API ROOT 없음
## -> 무슨 말...?

urlpatterns = [
    #localhost/post == ListView
    path('post/', views.PostList.as_view()),
    #localhost/post/<pk> == DetailView
    path('post/<int:pk>', views.PostDetail.as_view()),
]

# 이건 무슨 코드..?
urlpatterns = format_suffix_patterns(urlpatterns)
#1.format_suffix_patterns : 위 함수를 통해 특정 포맷을 간단하고 명확하게 참조할 수 있음(???). 필수는 아님
#2.format_suffix_patterns : 위 함수를 이용하면 URL을 사용할 때 데이터 형식(원시 json이나 html)을 지정할 수 있음. 패턴의 모든 URL에 사용할 형식을 추가
#3. https://github.com/KimDoKy/DjangoRestFramework-Tutorial/blob/master/doc/Django%20REST%20Framework%20-%2022.%20Format%20suffixes.md
#위 함수는 제공된 각 URL 패턴에 추가된 형식 접미사 패턴을 포함하는 URL 패턴 List를 반환함
#그리고 위 함수를 사용하는 경우 'format' 키워드 인수를 views.py에 정의된 함수나 클래스에 추가해야한다.