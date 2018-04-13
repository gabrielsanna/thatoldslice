document.addEventListener('DOMContentLoaded', () => {
	document.querySelector('#back-link').onclick = () => {
		processBackLink();
	}
});

function processBackLink() {
	window.history.back();
}