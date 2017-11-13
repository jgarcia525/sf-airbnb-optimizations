function doFirst() {
	var button = document.getElementById("button");
	button.addEventListener("click", saveData, false);
}

function saveData() {
	var latitude = document.getElementById("latitude").value;
	var longitude = document.getElementById("longitude").value;
	// sessionStorage.setItem(latitude, longitude);
	var blob = new Blob([latitude, longitude],{type = "text/plain;chairset=utf-8"});
	saveAs(blob, "input-file.txt")
}

window.addEventListener("load", doFirst, false)