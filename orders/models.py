from django.db import models

# Create your models here.

# Model for entrees/menu options
class Entree(models.Model):
	# Set up choices for 'size' dropdown
	LARGE = 'Large'
	SMALL = 'Small'
	NONE = 'None'
	SIZE_CHOICES = (
		(LARGE, 'Large'),
		(SMALL, 'Small'),
		(NONE, 'None')
	)

	# Set up choices for 'entree_type' dropdown
	REGULARPIZZA = 'Regular Pizza'
	SICILIANPIZZA = 'Sicilian Pizza'
	SUB = 'Sub'
	PASTA = 'Pasta'
	SALAD = 'Salad'
	DINNERPLATTER = 'Dinner Platter'
	TYPE_CHOICES = (
		(REGULARPIZZA, 'Regular Pizza'),
		(SICILIANPIZZA, 'Sicilian Pizza'),
		(SUB, 'Sub'),
		(PASTA, 'Pasta'),
		(SALAD, 'Salad'),
		(DINNERPLATTER, 'Dinner Platter'),
	)

	# Declare fields for the model
	name = models.CharField(max_length=100)
	entree_type = models.CharField(max_length=14, choices=TYPE_CHOICES, default=REGULARPIZZA)
	size = models.CharField(max_length=5, choices=SIZE_CHOICES, default=NONE)
	price = models.DecimalField(max_digits=5, decimal_places=2)

	def __str__(self):
		if "topping" in self.name:
			nameString = self.name.replace('toppings', 'topping')
		else:
			nameString = self.name

		return f"{nameString} {self.entree_type.lower()} ({self.size}): ${self.price}"

# Model for toppings on pizzas (and Steak+Cheese subs)
class PizzaTopping(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return f"{self.name}"

# Model for orders
class CustomerOrder(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	submitted_at = models.DateTimeField(auto_now_add=True)
	order_submitted = models.BooleanField(default=False)
	order_completed = models.BooleanField(default=False)
	user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	entree_included = models.ManyToManyField(Entree, through='MealsInOrder')

	def __str__(self):
		if self.order_submitted:
			submitted = "Submitted"
		else:
			submitted = "Unsubmitted"

		return f"{submitted} order by {self.user} at {self.created_at}"

# Model for the relationship between orders and the meals in those orders
# We need a custom model for this so we can add toppings as an additional
#   field to the relationship.
class MealsInOrder(models.Model):
	order = models.ForeignKey('CustomerOrder', on_delete=models.CASCADE)
	food_item = models.ForeignKey('Entree', on_delete=models.CASCADE)
	toppings = models.ManyToManyField(PizzaTopping, blank=True, related_name="pizzas")

	def __str__(self):
		if "Salad" in self.food_item.name and self.food_item.entree_type != "Dinner Platter":
			nameString = self.food_item.name.replace(" Salad", "")
		else:
			nameString = self.food_item.name.lower()

		if self.food_item.size == "None":
			sizeString = ""
		else:
			sizeString = f"{self.food_item.size} "

		return f"{sizeString}{nameString} {self.food_item.entree_type.lower()} (${self.food_item.price})"

