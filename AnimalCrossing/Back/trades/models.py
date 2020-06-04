from django.db import models
from django.conf import settings

class Article(models.Model):
    # 필수: title, content, user, category, sort
    # 선택: image, name, price
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='articles', on_delete=models.CASCADE)
    username = models.CharField(max_length=50) # 아이디 paik11012
    title = models.CharField(max_length=20)
    content = models.TextField(max_length=800)
    image = models.CharField(max_length=800, blank=True) # 선택 가능s
    category = models.CharField(max_length=20)  # animal, fossil, painting, etc 중 하나
    name = models.CharField(max_length=30, blank=True)  # 각 카테고리의 디테일 이름 선택적
    sort = models.CharField(max_length=20)  # buy sell 표시용
    price = models.CharField(max_length=20, blank=True)  # 가격 입력하거나 빈칸 가능(협의)
    created_at = models.DateTimeField(auto_now_add=True)  # 만들어졌을 때 기록하겠다 강조!!!!!!!!!!!
    updated_at = models.DateTimeField(auto_now=True)  # 언제든지 시간 기록하겠다
    def __str__(self):
        return self.title


class Comment(models.Model):
    # article instance가 comment를 역참조 할 수 있는 이름 정의
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')  # 타입 자체가 foreign key 1:n관계 만들 때에는 1이 먼저 선언되고 n이 선언되어야 한다 //
    content = models.TextField(max_length=200)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comments', on_delete=models.CASCADE)
    username = models.CharField(max_length=50) # 아이디 paik11012
    class Meta:
        ordering = ['-pk']  # 역순 ('-pk',)도 가능
    def __str__(self):
        return self.content