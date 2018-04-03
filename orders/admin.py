from django.contrib import admin
from .models import *

# Register your models here.

class PizzaToppingAdmin(admin.ModelAdmin):
	pass

admin.site.register(RegularPizza)
admin.site.register(SicilianPizza)
admin.site.register(PizzaTopping, PizzaToppingAdmin)
admin.site.register(Sub)
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(DinnerPlatter)

