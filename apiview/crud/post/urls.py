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