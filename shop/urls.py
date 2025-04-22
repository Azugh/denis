from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path('<int:n>', views.shopitem_detail, name='shopitem_detail'),
    path('cart', views.cart, name='cart'),
    path('history', views.history, name='history'),
    path('history/<int:n>', views.order_detail, name='order_detail'),
    path('cart/add/<int:n>/', views.cart_add, name='cart_add'),
    path('cart/delete/<int:n>/', views.cart_delete, name='cart_delete'),
    path('cart/update/<int:n>/', views.cart_update, name='cart_update')
]