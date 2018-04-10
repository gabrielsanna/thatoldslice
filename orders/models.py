from django.db import models

# Create your models here.
class Entree(models.Model):
    LARGE = 'Large'
    SMALL = 'Small'
    NONE = 'None'
    SIZE_CHOICES = (
        (LARGE, 'Large'),
        (SMALL, 'Small'),
        (NONE, 'None')
    )

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

    name = models.CharField(max_length=100)
    entree_type = models.CharField(max_length=14, choices=TYPE_CHOICES, default=REGULARPIZZA)
    size = models.CharField(max_length=5, choices=SIZE_CHOICES, default=NONE)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.entree_type} {self.name.lower()} pizza ({self.size}): ${self.price}"

class PizzaTopping(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class CustomerOrder(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order_submitted = models.BooleanField(default=False)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
    	if self.order_submitted:
    		submitted = "Submitted"
    	else:
    		submitted = "Unsubmitted"

    	return f"{submitted} order by {self.user} at {self.created_at}"

