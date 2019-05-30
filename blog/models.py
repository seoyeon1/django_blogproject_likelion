from django.db import models

# Create your models here.

class Blog(models.Model):#blog C에서 어떤 D를 처리할지 정의.
    title = models.CharField(max_length = 200)#title
    pub_date = models.DateTimeField('date published')#날짜, 시간알아내는 변수 사용
    body = models.TextField()#body:긴 글의 형식 저장하기 위해 textfield 사용

    def __str__(self):#str : (자기를) 문자열화 해주는 함수 선언. 블로그에서 title로 해둔 게 보이게 함.
        return self.title#title이라는 변수를 지정해서 자기 자신의 title 리턴

    def summary(self):
        return self.body[:100]#body속 글자를 100개 까지만 보이게 해줌. 100자 넘어가는 거는 detail가서 볼 수 있음.