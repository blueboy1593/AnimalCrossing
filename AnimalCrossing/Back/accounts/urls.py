from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('check_password/<int:user_id>/', views.check_password),
    path('withdraw/<int:user_id>/', views.withdraw),
    path('userprofile/<int:user_id>/', views.userprofile),
    path('change/<int:user_id>/', views.change),
    path('login/', views.UserLoginAPIView.as_view(),name='login')

]

