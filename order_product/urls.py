from django.urls import path
from . import views

urlpatterns = [
    path('order_item/', views.OrderItemView.as_view()),
    path('item/', views.ItemView.as_view())
]
