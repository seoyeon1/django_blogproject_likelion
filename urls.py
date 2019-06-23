"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import blog.views
import portfolio.views
from django.conf import settings
from django.conf.urls.static import static 
import accounts.views
urlpatterns = [
    #url를 효율적을 사용하기 위해 (계층적으로) 각 app마다 urls.py 추가, 거기에 path 작성. (app별로 url관리)
    #project에서는 각 app에서 url을 include해와서(가져와서) 사용. => code를 간결하게 관리 가능.
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')), #blog(app) 속 urls.py로 부터 가져오기(include) 위한 path
    path('portfolio/', include('portfolio.urls')), # portfolio(app) 속 ~
    path('accounts/', include('accounts.urls')), # accounts(app) 속 ~
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
