from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import serializers
from rest_framework.response import Response
from .serializers import ShowUserDetailSerializer, ShowSerializer, ShowcommentSerializer, ShowUpdateSerializer, ShowcommentUpdateSerializer
from .models import Show, Showcomment
from accounts.models import User 
from rest_framework.authtoken.models import Token


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def write(request): # 거래소에 글 하나 올리기

  # fields = ['id', 'title', 'content', 'image', 'category', 'name', 'sort', 'price', 'created_at', 'updated_at', 'user']
  title = request.data.get('title')
  content = request.data.get('content')
  image = request.data.get('image')
  user_id = request.data.get('user_id') # 고유한 유저 번호 132 등
  username = request.data.get('username')
  # 할당하기 contents 이상하다 이거
  show = Show()
  show.title = title
  show.content = content
  show.image = image
  show.username = username
  user =  get_object_or_404(User, pk=user_id) 
  show.user = user
  show.save()
  serializer = ShowSerializer(instance=show)
  return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def list(request): # 모든 거래소 글 가져오기
  shows = Show.objects.all()
  serializer = ShowSerializer(shows, many=True)
  return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def detail(request, show_pk):
  show = get_object_or_404(Show, pk=show_pk)
  if request.method == 'GET':
    permission_classes = [AllowAny]
    serializer = ShowSerializer(show)
    return Response(serializer.data)

@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def detail_ud(request, show_pk):
  if request.method == "PUT":
    serializer = ShowUpdateSerializer(data = request.data, instance=show)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      return Response(serializer.data)
    else: Response({'message': 'put error'})
  else:
    show.delete()
    return Response({'message': 'show post is successfully deleted'})
    
# 이제 댓글
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def showcomment(request, show_pk):
  serializer = ShowcommentSerializer(data = request.data)
  user_id = request.data.get('user_id')
  if serializer.is_valid(raise_exception=True):
    serializer.save(show_id = show_pk, user_id=user_id)
  return Response(serializer.data)

@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def showcomment_ud(request, showcomment_pk):
  showcomment = get_object_or_404(Showcomment, pk=showcomment_pk)
  if request.method == 'PUT':
    serializer = ShowcommentUpdateSerializer(data=request.data, instance=showcomment)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      return Response({'message':'completed comment update'})
  else:
    showcomment.delete()
    return Response({'message': 'completed comment delete'})

