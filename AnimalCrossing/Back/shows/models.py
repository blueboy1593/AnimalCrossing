from django.db import models
from django.conf import settings

class Show(models.Model):
    # 필수: title, content, user, username
    # 선택: image
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='shows', on_delete=models.CASCADE)
    username = models.CharField(max_length=50) # 아이디 paik11012
    title = models.CharField(max_length=20)
    content = models.TextField(max_length=800)
    image = models.CharField(max_length=800, blank=True) # 선택 가능s
    created_at = models.DateTimeField(auto_now_add=True)  # 만들어졌을 때 기록하겠다
    updated_at = models.DateTimeField(auto_now=True)  # 언제든지 시간 기록하겠다
    def __str__(self):
        return self.title


class Showcomment(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE, related_name='showcomments')  # 타입 자체가 foreign key 1:n관계 만들 때에는 1이 먼저 선언되고 n이 선언되어야 한다 //
    content = models.TextField(max_length=200)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='showcomments', on_delete=models.CASCADE)
    username = models.CharField(max_length=50) # 아이디 paik11012
    class Meta:
        ordering = ['-pk']  # 역순 ('-pk',)도 가능
    def __str__(self):
        return self.content