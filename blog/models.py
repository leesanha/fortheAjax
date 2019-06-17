from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model): # Blog 라는 이름의 객체 틀(Model) 생성
    title = models.CharField(max_length=200) # title 라는 최대 200 글자의 문자 데이터 저장
    pub_date = models.DateTimeField('date published') # pub_date 라는 날짜 시간 데이터 저장
    body = models.TextField() # body 라는 줄글 문자 저장
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)

    # 이 객체를 가르키는 말을 title로 정하겠다
    def __str__(self):
        return self.title

class Comment(models.Model):
    body = models.TextField()
    #Blog 모델과 관계를 맺어준다. 1:N에서 N의 속성으로 들어간다.
    #on_delete는 관계를 맺고 있는 Blog 객체가 삭제되면 관련된 Comment도 삭제시킨다.
    blog = models.ForeignKey(Blog, on_delete = models.CASCADE, null = True)

    def __str__(self):
        return self.body