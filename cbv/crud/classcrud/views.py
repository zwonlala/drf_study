from django.shortcuts import render
from django.utils import timezone

from django.urls import reverse_lazy #get_absolute_url(), reverse() 알아보기
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import ClassBlog

# Create your views here.
class BlogView(ListView):
    model = ClassBlog
    # html 템플릿 : 블로그 리스트를 담은 html : (소문자모델)_list.html

    # defalut 탬플릿 이름이 아닌 다른 이름으로 할때
    # template_name = 'classcrud/list.html'

    # 탬플릿으로 보내줄 모델이 여러가지 인 경우(서로 다른 객체 목록을 구분하는 방법)
    # context_object_name = 'blog_list'

class BlogCreate(CreateView):
    model = ClassBlog
    fields = ['title', 'body']
    success_url = reverse_lazy('list')
    # html 템플릿 : form (입력공간)을 가지고 있는 html : (소문자모델)_from.html


class BlogDetail(DetailView):
    model = ClassBlog
    # html 템플릿 : 상세 페이지를 담은 html : (소문자모델)_detail.html

class  BlogUpdate(UpdateView):
    model = ClassBlog
    fields = ['title', 'body']
    success_url = reverse_lazy('list')
    # html 템플릿 : form (입력공간)을 가지고 있는 html : (소문자모델)_from.html

class BlogDelete(DeleteView):
    model = ClassBlog
    success_url = reverse_lazy('list')
    # html 템플릿 : "이거 정말 지울꺼야라고 묻는" html : (소문자모델)_confirm_delete.html
