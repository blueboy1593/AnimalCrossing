from django.urls import path
from . import views

urlpatterns = [
  path('write/', views.write, name='write'), # 거래글 올리기 
  path('list/', views.list, name='list'), # 모든 거래글 가져오기
  path('detail/<int:show_pk>/', views.detail, name="detail"), # update detail delete
  # comments C R U D 가능
  path('comment/<int:show_pk>/', views.showcomment, name='showcomment'),
  path('comment_ud/<int:showcomment_pk>/', views.showcomment_ud, name='showcomment_ud'), # update delete
]