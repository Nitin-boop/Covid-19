

function findHSP() {
	console.log("FIND button clicked");
	var hsp = document.getElementById("location");
	var findhsp = document.getElementById("uifindHSP");
	var url =  "http://127.0.0.1:5000/get_location";
	console.log("OLA,It's working until POST");
	$.post(url, {
		"hsp" : hsp.value 
	} , function(data,status) {
	findhsp.innerHTML = "<h2>" + data.Hospital.toString() + "</h2>";
	console.log(status);
	});
}

window.onload = onPageLoad;