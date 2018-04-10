from django.contrib import admin
from .models import *

# Register your models here.

class MealsInOrderInline(admin.TabularInline):
	model = MealsInOrder
	extra = 1

class CustomerOrderAdmin(admin.ModelAdmin):
    inlines = (MealsInOrderInline,)

admin.site.register(Entree)
admin.site.register(PizzaTopping)
admin.site.register(CustomerOrder, CustomerOrderAdmin)
