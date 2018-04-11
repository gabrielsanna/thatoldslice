from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", auth_views.login, name="login"),
    path("logout/", auth_views.logout, name="logout"),
    path("register/", views.register, name="register"),
    path("menu/", views.menu, name="menu"),
    path("orders/", views.orders, name="orders"),
    path("order/<int:order_id>", views.single_order, name="single order"),
    path("cart/", views.cart, name="cart"),
]
