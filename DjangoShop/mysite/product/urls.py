from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.ProductList.as_view(), name='product_list'),
    path('<int:product_id>/', views.ProductDetail.as_view(), name='product_detail'),
    path('add-to-cart/<int:product_id>/', views.addToCart, name='add_to_cart'),
    path('remove-from-cart/<int:product_id>/', views.removeFromCart, name='remove_from_cart'),
    path('cart/', views.Cart.as_view(), name='cart'),
]