document.addEventListener('DOMContentLoaded', () => {
	// Get all the buttons that may require toppings
	var pizzaButtons = document.getElementsByClassName("pizza-btn");

    Array.from(pizzaButtons).forEach(function(element) {
      element.onclick = (event) => {
			processPizzaButton();
			event.preventDefault();
		}
    });

	document.querySelector('#regular-pizza-option-group').onclick = () => {
		processRegularPizzaButton();
	}

	document.querySelector('#sicilian-pizza-option-group').onclick = () => {
		processSicilianPizzaButton();
	}
});

function processPizzaButton() {
	
}

function processRegularPizzaButton() {
	document.querySelector('#large-regular-pizza-group').classList.toggle("hidden");
	document.querySelector('#small-regular-pizza-group').classList.toggle("hidden");
}

function processSicilianPizzaButton() {
	document.querySelector('#large-sicilian-pizza-group').classList.toggle("hidden");
	document.querySelector('#small-sicilian-pizza-group').classList.toggle("hidden");	
}
