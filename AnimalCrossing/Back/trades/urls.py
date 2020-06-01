from django.urls import path
from . import views

urlpatterns = [
  # articles C R U D 가능
  path('write/', views.write, name='write'), # trades/write/ 로 접속시 거래글 올리기 
  path('list/', views.list, name='list'), # 모든 거래글 가져오기
  path('list/etc/', views.etclist ,name='etclist'), # 1개 카테고리 거래글 뭉치 가져오기
  path('list/<str:category>/<str:name>/', views.namelist ,name='namelist'), # aninaml/Bianca
  path('detail/<int:article_pk>/', views.detail, name="detail"), # update detail delete
  # comments C R U D 가능
  path('comment/<int:article_pk>/', views.comment, name='comment'),
  path('comment_ud/<int:comment_pk>/', views.comment_ud, name='comment_ud'), # update delete
]

