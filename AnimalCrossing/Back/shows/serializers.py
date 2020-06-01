from rest_framework import serializers
from .models import Show, Showcomment
from accounts.models import User

class ShowcommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Showcomment
    fields = ['id', 'show', 'content', 'user_id', 'created_at', 'updated_at', 'username']

class ShowSerializer(serializers.ModelSerializer):
  showcomments = ShowcommentSerializer(many=True)
  class Meta:
    model = Show
    fields = ['id', 'title', 'content', 'image', 'created_at', 'updated_at', 'user_id', 'showcomments', 'username']

class ShowUserDetailSerializer(serializers.ModelSerializer):
  shows = ShowSerializer(many=True)
  showcomments = ShowcommentSerializer(many=True)
  class Meta:
    model = User
    fields = ['id', 'email', 'password', 'shows', 'showcomments', 'username']
  
class ShowUpdateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Show
    fields = ['id', 'title', 'content', 'image', 'created_at', 'updated_at', 'user_id']

class ShowcommentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
      model = Showcomment
      fields = ['id', 'show', 'content', 'user_id', 'created_at', 'updated_at', 'username']