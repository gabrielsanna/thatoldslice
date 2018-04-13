document.addEventListener('DOMContentLoaded', () => {
	// Get all the buttons that may require toppings
	var pizzaButtons = document.getElementsByClassName("pizza-btn");

    Array.from(pizzaButtons).forEach(function(element) {
		element.addEventListener('click', processPizzaButton);
    });

	document.querySelector('#regular-pizza-option-group').onclick = () => {
		processRegularPizzaButton();
	}

	document.querySelector('#sicilian-pizza-option-group').onclick = () => {
		processSicilianPizzaButton();
	}
});

function processPizzaButton(event) {
	event.preventDefault();
	pizzaType = this.innerHTML.split("<br>")[0];

	switch(pizzaType) {
		case "1 topping":
			maxToppings = 1;
			break;
		case "2 toppings":
			maxToppings = 2;
			break;
		case "3 toppings":
			maxToppings = 3;
			break;
		case "Special":
			maxToppings = 5;
			break;
		default:
			maxToppings = 0;
	}

	if(maxToppings > 0) {
		$('#toppingsModal').modal({
			focus: true
		});

		document.querySelector('#num-toppings').innerHTML = maxToppings;

		if (maxToppings === 1) {
			document.querySelector('#plural-toppings').innerHTML = "";
		}
	}
}

function processRegularPizzaButton() {
	document.querySelector('#large-regular-pizza-group').classList.toggle("hidden");
	document.querySelector('#small-regular-pizza-group').classList.toggle("hidden");
}

function processSicilianPizzaButton() {
	document.querySelector('#large-sicilian-pizza-group').classList.toggle("hidden");
	document.querySelector('#small-sicilian-pizza-group').classList.toggle("hidden");	
}
