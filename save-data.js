function doFirst() {
	var button = documnet.getElementById("button");
	button.addEventListener("click", saveData, false);
}

function saveData() {
	var latitude = document.getElementById("latitude").value;
	var longitude = document.getElementById("longitude").value;
	sessionStorage.setItem(latitude, longitude);
}

window.addEventListener("load", doFirst, false)