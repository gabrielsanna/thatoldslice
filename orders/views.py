import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.utils.datastructures import MultiValueDictKeyError

from .models import *

# Function to get the number of new orders for admins
def get_pending_orders(request):
	if request.user.is_superuser:
		pendingOrders = CustomerOrder.objects.filter(order_submitted=True).filter(order_completed=False)
		return len(pendingOrders)
	else:
		return 0

# Create your views here.

# Homepage with sweet public domain hero image
def index(request):
	if request.user.is_authenticated:
		AdminPendingOrders = get_pending_orders(request)

		context = {
			"PendingOrders": CustomerOrder.objects.filter(user=request.user).filter(order_submitted=True).filter(order_completed=False),
			"CompletedOrders": CustomerOrder.objects.filter(user=request.user).filter(order_submitted=True).filter(order_completed=True),
			"AdminPendingOrders": AdminPendingOrders,
		}
	else:
		context = {}

	return render(request, "orders/index.html", context)

# Page to register a new user
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

# Query all the entrees in the database and build the menu
def menu(request):
	AdminPendingOrders = get_pending_orders(request)

	context = {
		"PizzaToppings": PizzaTopping.objects.all(),
		"SteakCheeseToppings": SteakCheeseTopping.objects.all(),
		"LargeRegularPizzas": Entree.objects.filter(entree_type="Regular Pizza").filter(size="Large"),
		"SmallRegularPizzas": Entree.objects.filter(entree_type="Regular Pizza").filter(size="Small"),
		"LargeSicilianPizzas": Entree.objects.filter(entree_type="Sicilian Pizza").filter(size="Large"),
		"SmallSicilianPizzas": Entree.objects.filter(entree_type="Sicilian Pizza").filter(size="Small"),
		"LargeSubs": Entree.objects.filter(entree_type="Sub").filter(size="Large"),
		"SmallSubs": Entree.objects.filter(entree_type="Sub").filter(size="Small"),
		"Pastas": Entree.objects.filter(entree_type="Pasta"),
		"Salads": Entree.objects.filter(entree_type="Salad"),
		"LargeDinnerPlatters": Entree.objects.filter(entree_type="Dinner Platter").filter(size="Large"),
		"SmallDinnerPlatters": Entree.objects.filter(entree_type="Dinner Platter").filter(size="Small"),
		"AdminPendingOrders": AdminPendingOrders,
	}

	return render(request, "orders/menu.html", context)

# Add an item to cart (used for everything except pizzas)
def add_to_cart(request):
	if request.user.is_authenticated:
		entreeId = int(request.POST["entree"])

		# Instantiate objects
		currentUser = User.objects.get(id=request.user.id)
		currentEntree = Entree.objects.get(id=entreeId)

		# Check if there's an unsubmitted order and create one if not
		try:
			cartOrder = CustomerOrder.objects.filter(user=currentUser).get(order_submitted="False")
		except ObjectDoesNotExist:
			cartOrder = CustomerOrder.objects.create(user=currentUser)

		newEntree = MealsInOrder(order=cartOrder, food_item=currentEntree)
		newEntree.save()

		messages.add_message(request, messages.INFO, f"Added to cart: {str(newEntree)}")

		return redirect('menu')
	else:
		return redirect('login')

# Function to add a pizza to cart
# Pizzas get special treatment because they require use of the "toppings" relationship
# This function also applies to Steak and Cheese subs
def add_pizza_to_cart(request):
	if request.user.is_authenticated:
		pizzaId = int(request.POST["pizzaId"])
		try:
			toppingIdList = request.POST["checkedToppings"]
			toppingIdList = toppingIdList.split(',')
		except MultiValueDictKeyError:
			toppingIdList = []

		# Instantiate all our objects
		currentUser = User.objects.get(id=request.user.id)
		currentPizza = Entree.objects.get(id=pizzaId)
		toppingList = []
		if currentPizza.entree_type == "Sub":
			for toppingId in toppingIdList:
				topping = SteakCheeseTopping.objects.get(id=int(toppingId))
				toppingList.append(topping)
		else:
			for toppingId in toppingIdList:
				topping = PizzaTopping.objects.get(id=int(toppingId))
				toppingList.append(topping)

		# Check if there's an unsubmitted order and create one if not
		try:
			cartOrder = CustomerOrder.objects.filter(user=currentUser).get(order_submitted="False")
		except ObjectDoesNotExist:
			cartOrder = CustomerOrder.objects.create(user=currentUser)

		# Save our entree into the order
		newPizza = MealsInOrder(order=cartOrder, food_item=currentPizza)
		newPizza.save()

		# Check if we're dealing with a Sub or a Pizza and add toppings accordingly
		if currentPizza.entree_type == "Sub":
			for topping in toppingList:
				newPizza.subToppings.add(topping)
		else:
			for topping in toppingList:
				newPizza.toppings.add(topping)

		# Post a success message to appear on page load
		messages.add_message(request, messages.INFO, f"Added to cart: {str(newPizza)}")

		return "Success"
	else:
		return redirect('login')

# Delete an item from the cart and reload the cart
def delete(request, order_entree_id):
	# Get the item to be deleted from the database
	itemToDelete = MealsInOrder.objects.get(id=order_entree_id)

	itemToDelete.delete()

	messages.add_message(request, messages.INFO, f"Item deleted.")

	return redirect('cart')

# View to display all of a user's past submitted orders
def orders(request):
	AdminPendingOrders = get_pending_orders(request)

	context = {
		"PastOrders": CustomerOrder.objects.filter(user=request.user).filter(order_submitted=True).order_by('-submitted_at'),
		"AdminPendingOrders": AdminPendingOrders,
	}

	if request.user.is_authenticated:
		return render(request, "orders/orders.html", context)
	else:
		return redirect('login')

# View to display all user's past orders to administrators
def all_orders(request):
	AdminPendingOrders = get_pending_orders(request)

	if request.user.is_superuser:
		allOrders = CustomerOrder.objects.filter(order_submitted=True).order_by('-submitted_at')

		context = {
			"allOrders": allOrders,
			"AdminPendingOrders": AdminPendingOrders,
		}

		return render(request, "orders/all-orders.html", context)
	else:
		return render(request, "orders/access-denied.html")

# Mark an order as "completed" (no longer pending)
def complete_order(request, order_id):
	if request.user.is_superuser:
		orderToComplete = CustomerOrder.objects.get(id=order_id)
		orderToComplete.order_completed = True
		orderToComplete.save()

		return redirect('all orders')
	else:
		return render(request, "orders/access-denied.html")

# Mark a completed order as incomplete (if something went wrong)
def reopen(request, order_id):
	if request.user.is_superuser:
		orderToComplete = CustomerOrder.objects.get(id=order_id)
		orderToComplete.order_completed = False
		orderToComplete.save()

		return redirect('all orders')
	else:
		return render(request, "orders/access-denied.html")

# Page to view the items in a single historical order
def single_order(request, order_id):
	OrderRequested = CustomerOrder.objects.get(id=order_id)
	EntreesInOrder = MealsInOrder.objects.filter(order=OrderRequested)
	OrderUser = OrderRequested.user

	# Total up the cost of the order
	Total = 0
	for entree in EntreesInOrder:
		Total += entree.food_item.price

		if entree.food_item.entree_type == "Sub":
			for topping in entree.subToppings.all():
				Total += topping.price

	context = {
		"OrderRequested": OrderRequested,
		"EntreesInOrder": EntreesInOrder,
		"Total": Total,
		"AdminPendingOrders": AdminPendingOrders,
	}

	if request.user == OrderUser or request.user.is_superuser:
		return render(request, "orders/single-order.html", context)
	else:
		return render(request, "orders/access-denied.html")

# View to display a user's unsubmitted order
def cart(request):
	AdminPendingOrders = get_pending_orders(request)

	try:
		CartOrder = CustomerOrder.objects.filter(user=request.user).get(order_submitted=False)
		OrderEntrees = MealsInOrder.objects.filter(order=CartOrder)

		# Total up the cost of the order
		Total = 0
		for entree in OrderEntrees:
			Total += entree.food_item.price

			if entree.food_item.entree_type == "Sub":
				for topping in entree.subToppings.all():
					Total += topping.price

		context = {
			"OrderEntrees": OrderEntrees,
			"Total": Total,
			"AdminPendingOrders": AdminPendingOrders,
		}
	except ObjectDoesNotExist:
		context = {
			"AdminPendingOrders": AdminPendingOrders,
		}

	return render(request, "orders/cart.html", context)

# Submit an order (clears cart, shows up to admins)
def submit(request):
	try:
		CartOrder = CustomerOrder.objects.filter(user=request.user).get(order_submitted=False)
		CartOrder.order_submitted = True
		CartOrder.submitted_at = datetime.datetime.now()
		CartOrder.save()

		return render(request, "orders/submitted.html")
	except TypeError:
		return render(request, "orders/access-denied.html")

