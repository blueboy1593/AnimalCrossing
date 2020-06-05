from django.urls import path
from . import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
schema_view = get_schema_view(
    openapi.Info(
        title='collects API',
        default_version='v1',
        description='동물의 숲 도감 API 서비스입니다.',
    ),
    permission_classes=(AllowAny,)
)

urlpatterns = [
    # path('insert/', views.excel_to_list),
    path('fishes/', views.fishes, name='fish_list'),
    path('insects/', views.insects, name='insect_list'),
    path('fossils/', views.fossils, name='fossil_list'),
    path('paintings/', views.paintings, name='painting_list'),
    path('animals/', views.animals, name='animal_list'),
    path('docs/', schema_view.with_ui('redoc'), name='api_docs'),
    path('swagger/', schema_view.with_ui('swagger'), name='swagger')
]