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

	document.querySelector('#sub-option-group').onclick = () => {
		processSubButton();
	}
});

function processPizzaButton(event) {
	event.preventDefault();
	pizzaType = this.innerHTML.split("<br>")[0];
	pizzaId = this.value;

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

	// Disable the add to cart button
	enableDisableCartButton(maxToppings);

	if(maxToppings > 0) {
		$('#toppingsModal').modal({
			focus: true
		});

		document.querySelector('#num-toppings').innerHTML = maxToppings;

		if (maxToppings === 1) {
			document.querySelector('#plural-toppings').innerHTML = "";
		} else {
			document.querySelector('#plural-toppings').innerHTML = "s";
		}

		// Add listeners for topping checkboxes
		var toppingCheckboxes = document.getElementsByClassName("topping-btn");

    	Array.from(toppingCheckboxes).forEach(function(element) {
			element.onclick = (event) => {
				// Use a Promise so checks are counted as they happen
				Promise.resolve().then(_ => {
					enableDisableCartButton(maxToppings);
    			});
			}
		});

		// Add listener for "Add to Cart" button
		document.querySelector('#modal-add-to-cart-btn').onclick = () => {
			checkedToppings = checkCheckedToppings();
			processModalSubmitButton(pizzaId, checkedToppings);
		}
	}
}

// Loop through the list of topping checkboxes and gather the checked ones
function checkCheckedToppings() {
	var checkboxList = document.getElementsByName("topping");
	var toppingsChecked = [];

	for (var i = 0; i < checkboxList.length; i++) {
		if (checkboxList[i].checked) {
        	toppingsChecked.push(checkboxList[i].value);
		}
	}

	if (toppingsChecked.length > 0) {
		return toppingsChecked;
	} else {
		return null;
	}
}

// Check how many toppings are checked. If it's greater or
// less than the number required, disable Add to Cart button.
function enableDisableCartButton(maxToppings) {
	var checkboxList = document.getElementsByName("topping");
	checkedCount = 0;

	for (var i = 0; i < checkboxList.length; i++) {
		if (checkboxList[i].checked) {
			checkedCount++;
		}
	}

	if (maxToppings == checkedCount) {
		document.querySelector('#modal-add-to-cart-btn').disabled = false;
	} else {
		document.querySelector('#modal-add-to-cart-btn').disabled = true;
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

function processSubButton() {
	document.querySelector('#large-sub-list').classList.toggle("hidden");
	document.querySelector('#small-sub-list').classList.toggle("hidden");	
}

function processModalSubmitButton(pizzaId, checkedToppings) {
	const request = new XMLHttpRequest();
	request.open('POST', '/add-pizza-to-cart/');
	request.setRequestHeader("X-CSRFToken", csrf_token)

	request.onload = () => {
		window.location.reload(true);
	}

	const data = new FormData();
	data.append('pizzaId', pizzaId);
	data.append('checkedToppings', checkedToppings);

	request.send(data);
	return false;
}
