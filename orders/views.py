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
		"LargeRegularPizzas": Pizza.objects.filter(type="Regular").filter(size="Large"),
		"SmallRegularPizzas": Pizza.objects.filter(type="Regular").filter(size="Small"),
		"LargeSicilianPizzas": Pizza.objects.filter(type="Sicilian").filter(size="Large"),
		"SmallSicilianPizzas": Pizza.objects.filter(type="Sicilian").filter(size="Small"),
	}

	return render(request, "orders/menu.html", context)