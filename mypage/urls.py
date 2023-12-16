from django.urls import path
from .views import User

from . import views

app_name = "mypage"

urlpatterns = [
    path('', views.index, name='list'),
    path('<int:user_id>/', views.detail, name='detail'),
    path('create/', views.create.as_view(), name='create'),
]