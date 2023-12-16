from django.urls import path
from .views import PaymentView

from . import views

app_name = "bag"

urlpatterns = [
    path('', views.index, name='list'),
    path('<int:bag_id>/', views.detail, name='detail'),
    path('create/', views.create.as_view(), name='create'),
    path('<int:bag_id>/payment/', PaymentView.as_view(), name='payment'),
]
