from django import forms
from .models import Blog
#form(model기반의 입력공간): 필요할 때마다 하나하나 html <form>태그 만들지 않아도 됨.
#(model에서 class 만드는 것과 유사. html의 <form> 과 매핑됨)

class BlogForm(forms.ModelForm):    #model 기반 입력공간
    class Meta:     #inner class(기반 model, model의 어떤 항목들을 입력받을지)
        model = Blog    #기반 model(=Blog)
        fields = ['title', 'body']   #입력받을 항목들(시간,날짜는 views에서 직접 받을 예정)