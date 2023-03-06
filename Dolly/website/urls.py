# from django import views
from .import views
from django.urls import path

urlpatterns = [

    path('',views.Home, name="Home"),  
    path('About/',views.About,name="About") ,
    path('products/',views.products,name="products"),
    path('cart/',views.cart,name="cart"),
    path('checkout/',views.checkout,name="checkout"),

    path('update_item/',views.updateItem, name="update_item"),
    path('process_order/',views.processOrder,name="process_order")
    ]


