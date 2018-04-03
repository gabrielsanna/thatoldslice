from django.db import models

# Create your models here.
class RegularPizza(models.Model):
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

class SicilianPizza(models.Model):
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
