# 백 - 프론트 통신규약



## Vuex 혹은 localStorage에 담았으면 좋겠다고 생각하는 것

token과 username

(매번 글, 댓글 쓸 때마다 필요함)



## 1. Article

  # 필수: title, content, user_id, category, sort, username

  # 선택: image, name, price

```python
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='articles', on_delete=models.CASCADE) # user번호: 1
    username = models.CharField(max_length=50) # username: paik11012
    title = models.CharField(max_length=20)
    content = models.TextField(max_length=800)
    image = models.ImageField(blank=True) 
    category = models.CharField(max_length=20)  # animal, fossil, painting, etc 중 하나
    name = models.CharField(max_length=30, blank=True)  # 각 카테고리의 내 이름 선택적(예: Bianca)
    sort = models.CharField(max_length=20)  # buy sell 중 하나
    price = models.CharField(max_length=20, blank=True)
```

name과 같은 경우 고유 아이템 이름으로 설정(예시: Bianca, 강꼬치고기 등)

나중에 animal, fossil, painting, etc로 필터링 할 예정(백 담당)

나중에 buy, sell로 필터링 할 예정(프론트 담당)

###  postman 예시

```json
{
    "user_id": 1,
    "username": "mjmj"
    "title": "제목",
    "content":"example",
    "category": "animal",
    "name": "Bianca",
    "sort": "sell",
    "price": "20000벨",
}
```

etc 글쓰기와 같은 경우는 이미지 올리기 가능(firebase 혹은 imgur 생각 중)



## 2. Comment

```python
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments') #글 번호
    content = models.TextField(max_length=200)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comments', on_delete=models.CASCADE)
    username = models.CharField(max_length=50) # 아이디 paik11012
```

json

```json
{
    "article": 2,
    "content":"example comment",
    "user": 3,
    "username": "mjmj"
}
```



## 3. Signup

필요한 필드: email, username, password(이메일만 고유할 것)

username안 넣으려다 글 쓸때 아이디 필요해서 넣음

```
{
    "email": "mj@naver.com",
    "username":"minju",
    "password":"mjmj"
}
```

