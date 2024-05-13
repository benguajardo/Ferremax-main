from django.urls import path
from .views import *

urlpatterns = [
        path('', index, name="index"),
        path('shop/', shop, name="shop"),
        path('base/', base, name="base"),
        path('detail', detail, name="detail"),
        path('contact/', contact, name="contact"),
        path('checkout/', checkout, name="checkout"),
        path('cart/', cart, name="cart"),
        path('a', a, name="a"),

        # CRUD PRODUCTO
        path('addProduct', addProduct, name="addProduct"),
        path('updateProduct/<id>/', updateProduct, name="updateProduct"),
        path('deleteProduct/<id>/', deleteProduct, name="deleteProduct"),
        
        
]