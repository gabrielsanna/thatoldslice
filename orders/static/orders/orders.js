document.addEventListener('DOMContentLoaded', () => {
	try {
		document.querySelector('#back-link').onclick = () => {
			processBackLink();
		}
	} catch(e) {
		return;
	}
});

function processBackLink() {
	window.history.back();
}
