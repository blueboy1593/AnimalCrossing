from django.urls import path
from . import views


urlpatterns = [
    path('insert/', views.excel_to_list),
    # path('todos/<int:todo_id>/', views.todo_update_delete),
    # path('users/<int:user_id>/', views.user_detail),

]