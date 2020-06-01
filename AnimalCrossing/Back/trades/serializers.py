from rest_framework import serializers
from .models import Article, Comment
from accounts.serializers import UserSerializer
from accounts.models import User

class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = ['id', 'article', 'content', 'user_id', 'created_at', 'updated_at', 'username']

class ArticleSerializer(serializers.ModelSerializer):
  comments = CommentSerializer(many=True)
  class Meta:
    model = Article
    fields = ['id', 'title', 'content', 'image', 'category', 'name', 'sort', 'price', 'created_at', 'updated_at', 'user_id', 'comments', 'username']

class UserDetailSerializer(serializers.ModelSerializer):
  articles = ArticleSerializer(many=True)
  comments = CommentSerializer(many=True)
  class Meta:
    model = User
    fields = ['id', 'email', 'password', 'articles', 'comments', 'username']
  
class ArticleUpdateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Article
    fields = ['id', 'title', 'content', 'image', 'category', 'name', 'sort', 'price', 'created_at', 'updated_at', 'user_id']

class CommentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
      model = Comment
      fields = ['id', 'article', 'content', 'user_id', 'created_at', 'updated_at', 'username']