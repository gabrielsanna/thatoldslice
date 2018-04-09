from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

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
		"LargeRegularPizzas": Pizza.objects.filter(pizza_type="Regular").filter(size="Large"),
		"SmallRegularPizzas": Pizza.objects.filter(pizza_type="Regular").filter(size="Small"),
		"LargeSicilianPizzas": Pizza.objects.filter(pizza_type="Sicilian").filter(size="Large"),
		"SmallSicilianPizzas": Pizza.objects.filter(pizza_type="Sicilian").filter(size="Small"),
		"LargeSubs": Sub.objects.filter(size="Large"),
		"SmallSubs": Sub.objects.filter(size="Small"),
		"Pastas": Pasta.objects.all(),
		"Salads": Salad.objects.all(),
		"LargeDinnerPlatters": DinnerPlatter.objects.filter(size="Large"),
	}

	return render(request, "orders/menu.html", context)