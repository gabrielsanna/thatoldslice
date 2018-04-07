from django.db import models

# Create your models here.
class Pizza(models.Model):
	LARGE = 'Large'
	SMALL = 'Small'
	SIZE_CHOICES = (
		(LARGE, 'Large'),
		(SMALL, 'Small'),
	)

	REGULAR = 'Regular'
	SICILIAN = 'Sicilian'
	TYPE_CHOICES = (
		(REGULAR, 'Regular'),
		(SICILIAN, 'Sicilian'),
	)

	name = models.CharField(max_length=100)
	pizza_type = models.CharField(max_length=8, choices=TYPE_CHOICES, default=REGULAR)
	size = models.CharField(max_length=5, choices=SIZE_CHOICES, default=SMALL)
	price = models.DecimalField(max_digits=5, decimal_places=2)

	def __str__(self):
		return f"{self.pizza_type} {self.name.lower()} pizza ({self.size}): ${self.price}"

class PizzaTopping(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return f"{self.name}"

class Sub(models.Model):
	LARGE = 'Large'
	SMALL = 'Small'
	SIZE_CHOICES = (
		(LARGE, 'Large'),
		(SMALL, 'Small'),
	)

	name = models.CharField(max_length=100)
	price = models.DecimalField(max_digits=5, decimal_places=2)
	size = models.CharField(max_length=5, choices=SIZE_CHOICES, default=SMALL)

	def __str__(self):
		return f"{self.name} ({self.size}): ${self.price}"

class Pasta(models.Model):
	name = models.CharField(max_length=100)
	price = models.DecimalField(max_digits=5, decimal_places=2)

	def __str__(self):
		return f"{self.name}: ${self.price}"

class Salad(models.Model):
	name = models.CharField(max_length=100)
	price = models.DecimalField(max_digits=5, decimal_places=2)

	def __str__(self):
		return f"{self.name}: ${self.price}"

class DinnerPlatter(models.Model):
	LARGE = 'Large'
	SMALL = 'Small'
	SIZE_CHOICES = (
		(LARGE, 'Large'),
		(SMALL, 'Small'),
	)

	name = models.CharField(max_length=100)
	price = models.DecimalField(max_digits=5, decimal_places=2)
	size = models.CharField(max_length=5, choices=SIZE_CHOICES, default=SMALL)

	def __str__(self):
		return f"{self.name} ({self.size}): ${self.price}"
