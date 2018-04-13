from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ObjectDoesNotExist

from .models import *

# Create your views here.
def index(request):
	context = {}
	return render(request, "orders/index.html", context)

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=password)
			login(request, user)

			return redirect('index')
	else:
		form = UserCreationForm()
	return render(request, 'orders/register.html', {'form': form})

def menu(request):
	context = {
		"PizzaToppings": PizzaTopping.objects.all(),
		"LargeRegularPizzas": Entree.objects.filter(entree_type="Regular Pizza").filter(size="Large"),
		"SmallRegularPizzas": Entree.objects.filter(entree_type="Regular Pizza").filter(size="Small"),
		"LargeSicilianPizzas": Entree.objects.filter(entree_type="Sicilian Pizza").filter(size="Large"),
		"SmallSicilianPizzas": Entree.objects.filter(entree_type="Sicilian Pizza").filter(size="Small"),
		"LargeSubs": Entree.objects.filter(entree_type="Sub").filter(size="Large"),
		"SmallSubs": Entree.objects.filter(entree_type="Sub").filter(size="Small"),
		"Pastas": Entree.objects.filter(entree_type="Pasta"),
		"Salads": Entree.objects.filter(entree_type="Salad"),
		"LargeDinnerPlatters": Entree.objects.filter(entree_type="Dinner Platter").filter(size="Large"),
	}

	return render(request, "orders/menu.html", context)

def add_to_cart(request):
	if request.user.is_authenticated:
#		meal_name = request.POST["passenger"]
		pass
	else:
		return redirect('login')


# View to display all of a user's past submitted orders
def orders(request):
	context = {
		"PastOrders": CustomerOrder.objects.filter(user=request.user).filter(order_submitted=True),
	}

	if request.user.is_authenticated:
		return render(request, "orders/orders.html", context)
	else:
		return redirect('login')

def single_order(request, order_id):
	context = {
		"OrderRequested": CustomerOrder.objects.get(id=order_id),
		"Entrees": Entree.objects.prefetch_related('food_item__name')
	}

	orderUser = CustomerOrder.objects.get(id=order_id).user

	if request.user == orderUser:
		return render(request, "orders/single-order.html", context)
	else:
		return render(request, "orders/access-denied.html")

# View to display a user's unsubmitted order
def cart(request):
	try:
		CartOrder = CustomerOrder.objects.filter(user=request.user).get(order_submitted=False)
		OrderEntrees = CartOrder.entree_included.all()

		Total = 0
		for entree in OrderEntrees:
			Total += entree.price

		context = {
			"OrderEntrees": OrderEntrees,
			"Total": Total,
		}
	except ObjectDoesNotExist:
		context = {}

	return render(request, "orders/cart.html", context)

def submit(request):
	try:
		CartOrder = CustomerOrder.objects.filter(user=request.user).get(order_submitted=False)
		CartOrder.order_submitted = True
		CartOrder.save()

		return render(request, "orders/submitted.html")
	except TypeError:
		return render(request, "orders/access-denied.html")

