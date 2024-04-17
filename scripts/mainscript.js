// this used to check what code you entered to send you to the correct page, but this isnt used anymore. 

document.getElementById('codeinput').addEventListener("keyup", function(key) {
	if (key.keyCode != 13) return;
	submit(document.getElementById('codeinput').value.toLowerCase().split(" ").join(""));
})
let falseInputs = 0;
function submit(input) {
	if (input == "einmannhubschrauber") return window.open("http://www.henrimoe.de/", "_self");

	if (["musik", "music", "sheetmusic", "sheetmusicquizz", "sheetmusicquiz"].includes(input)) return window.open("sheet-music-quizz/index.html", "_self");

	document.getElementById('codeinput').value = "";
	falseInputs += 1;
	console.log(`There has/have been ${falseInputs} unknown or missspelled input(s).`);
	fehlermeldung(falseInputs);

}
function fehlermeldung(amount) {
	$('.errorcounter').text(amount);
	$('.codeinput').addClass("shakeanimation");
	setTimeout(function() {
		$('.codeinput').removeClass("shakeanimation");
	}, 750);

}

// checking whether JQuery is running or not. 
window.onload = function() {
    if (window.jQuery) {  
        // jQuery is loaded  
        console.log("JQuery works!");
    } else {
        // jQuery is not loaded
        console.log("-------JQuery doesn't work-------");
    }
}
