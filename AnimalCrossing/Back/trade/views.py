from django.shortcuts import render, get_object_or_404
from .models import Article, Comment
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import serializers
from rest_framework.response import Response
from .serializers import UserDetailSerializer, ArticleSerializer, CommentSerializer
from .models import Article, Comment
from accounts.models import User 


# Create your views here.
# Article crud, 댓글 crud

@api_view(['POST'])
@permission_classes([AllowAny])
def write(request): # 거래소에 글 하나 올리기
  # fields = ['id', 'title', 'content', 'image', 'category', 'name', 'sort', 'price', 'created_at', 'updated_at', 'user']
  title = request.data.get('title')
  content = request.data.get('content')
  image = request.data.get('image')
  category = request.data.get('category')
  name = request.data.get('name')
  sort = request.data.get('sort')
  price = request.data.get('price')
  user_id = request.data.get('user') # 고유한 유저 번호 132 등
  
  # 할당하기 contents 이상하다 이거
  article = Article()
  article.title = title
  article.content = content
  article.image = image
  article.category = category
  article.name = name
  article.sort = sort
  article.price = price
  user =  get_object_or_404(User, pk=user_id) # user와 연결 아이디 가져오기 paik11012
  article.user = user
  article.save()
  serializer = ArticleSerializer(instance=article)
  print(serializer.data)
  print('글쓰기 성공')
  return Response(serializer.data)