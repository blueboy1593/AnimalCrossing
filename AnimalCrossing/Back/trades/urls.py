from django.urls import path
from . import views

urlpatterns = [
  # articles C R U D 가능
  path('write/', views.write, name='write'), # trades/write/ 로 접속시 거래글 올리기 
  path('list/', views.list, name='list'), # 모든 거래글 가져오기
  path('detail/<int:article_pk>/', views.detail, name="detail"), # update detail delete
  # comments C R U D 가능
  path('comment/<int:article_pk>/', views.comment, name='comment')
]

