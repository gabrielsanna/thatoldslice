document.addEventListener('DOMContentLoaded', () => {
	try {
		document.querySelector('#back-link').onclick = () => {
			processBackLink();
		}
	} catch(e) {
		return;
	}

	document.querySelector('#regular-pizza-option-group').addEventListener('click', processRegularPizzaButton)

	try {
		document.querySelector('#regular-pizza-option-group').addEventListener('click', processRegularPizzaButton)
/*
		document.querySelector('#regular-pizza-option-group').onclick = () => {
			console.log("CLICK");
			processRegularPizzaButton();
		} */
	} catch(e) {
		console.log("Error");
		return;
	}
});

function processBackLink() {
	window.history.back();
}

function processRegularPizzaButton() {
	var sizes = document.getElementsByName("regular-pizza-option");
	var selectedSize;

	for(var i = 0; i < sizes.length; i++) {
		if(sizes[i].checked)
			selectedSize = sizes[i].value;
	}

	console.log("selectedSize");

	if (selectedSize === "Large") {
		document.querySelector('#large-regular-pizza-group').removeAttribute("display");
		document.querySelector('#small-regular-pizza-group').setAttribute("display", "none");
	} else {
		document.querySelector('#large-regular-pizza-group').setAttribute("display", "none");
		document.querySelector('#small-regular-pizza-group').removeAttribute("display");
	}
}
