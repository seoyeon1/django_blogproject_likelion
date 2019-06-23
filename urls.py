from django.contrib import admin
from django.urls import path
from . import views     #import blog.views 같은 의미.

urlpatterns = [     #이 app에서 다루는 path들 (code를 간결하게 관리)
    path('', views.home, name='home'),
    path('<int:blog_id>', views.detail, name='detail'),#path에 게시글마다의 아이디 값 받아서 보여줌.
    path('new/', views.new, name='new'),
    path('create', views.create, name='create'),#함수를 부를 때도 사용가능
    path('edit/<int:blog_id>', views.edit, name='edit'),
    path('delete/<int:blog_id>', views.delete, name='delete'),

    path('comment_add/<int:blog_id>', views.comment_add, name='comment_add'),
    path('comment_edit/<int:comment_id>', views.comment_edit, name='comment_edit'),
    path('comment_delete/<int:comment_id>', views.comment_delete, name='comment_delete'),
]