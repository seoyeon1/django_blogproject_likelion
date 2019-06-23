from django.contrib import admin
from django.urls import path
from . import views     #import accounts.views 같은 의미.

urlpatterns = [     #이 app에서 다루는 path들 (code를 간결하게 관리)

    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]