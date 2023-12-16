from django.urls import path
from .views import PaymentView

from . import views

app_name = "shoes"

urlpatterns = [
    path('', views.index, name='list'),
    path('<int:shoes_id>/', views.detail, name='detail'),
    path('create/', views.create.as_view(), name='create'),
    path('<int:shoes_id>/payment/', PaymentView.as_view(), name='payment'),
]
