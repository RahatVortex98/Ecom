from django.urls import path
from .views import AddToCartView, CartView,CheckoutView, OrderConfirmationView,Store,ProductDetail, UpdateCartView

urlpatterns = [
    
    path('',Store.as_view(),name='store'),
    path('cart/',CartView.as_view(),name='cart'),
    path('checkout/',CheckoutView.as_view(),name='checkout'),
    
    
    path('detail/<int:pk>/',ProductDetail.as_view(),name='detail'),
    
    path('add-to-cart/<int:product_id>/', AddToCartView.as_view(), name='add_to_cart'),
    path('update-cart/', UpdateCartView.as_view(), name='update_cart'),
    path('order-confirmation/', OrderConfirmationView.as_view(), name='order_confirmation'),

    
]
