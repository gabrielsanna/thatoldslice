from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
	path("", views.index, name="index"),
	path("login/", auth_views.login, name="login"),
	path("logout/", auth_views.logout, name="logout"),
	path("register/", views.register, name="register"),
	path("menu/", views.menu, name="menu"),
	path("add-to-cart/", views.add_to_cart, name="add to cart"),
	path("add-pizza-to-cart/", views.add_pizza_to_cart, name="add pizza to cart"),
	path("delete/<int:order_entree_id>", views.delete, name="delete"),
	path("orders/", views.orders, name="orders"),
	path("all-orders/", views.all_orders, name="all orders"),
	path("complete-order/<int:order_id>", views.complete_order, name="complete order"),
	path("reopen/<int:order_id>", views.reopen, name="reopen"),
	path("order/<int:order_id>", views.single_order, name="single order"),
	path("cart/", views.cart, name="cart"),
	path("submit-order/", views.submit, name="submit"),
]
