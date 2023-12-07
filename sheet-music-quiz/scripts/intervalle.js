// BASIC INITIALIZIATION
const buttonContainer = document.getElementById("button-container")
const amountButtons = buttonContainer.childElementCount;
var lastchosenImage
var lastchosenBGImage
const sleeptime = 500;
var blockInput = false;

// RANDOM IMAGE
var images = [
    "kleineTerz00.png",
    "großeTerz00.png",
    "großeTerz01.png",
    "Quarte00.png",
    "Quarte01.png",
    "Quarte02.png",
    "Tritonus00.png",
    "Quinte00.png",
    "Quinte01.png",
    "Quinte02.png",
    "Quinte03.png",
    "kleineSexte00.png",
    "kleineSexte01.png",
    "großeSexte00.png",
    "großeSexte01.png",
    "Oktave00.png",
    "Oktave01.png",
    "Oktave02.png",
    "Oktave03.png",
    "Oktave04.png",
    "None00.png",
];
function changeImage() {
    if (typeof slicedchosenImage != 'undefined') {
        document.getElementById(slicedchosenImage).style.backgroundColor = "black"; 
    }
    blockInput = false;
    chosenImage = images[Math.floor(Math.random() * images.length)];
    document.getElementById("change-img").src = `../images/${chosenImage}`;
    if (chosenImage == lastchosenImage) {
        changeImage()
    }   else {
        resetColor();
        lastchosenImage = chosenImage;
    }
}
changeImage()



// RESET COLOR
function resetColor() {
    for (let i = 0; i < buttonContainer.children.length; i++) {
        document.getElementById(buttonContainer.children[i].id).style.backgroundColor = "black";
    }
}

// BUTTONS
function buttonPressed(input) {
    if (blockInput) {
        console.log("WAIT FFS")
        return;
    }
    slicedchosenImage = chosenImage.replace(".png", "").slice(0,-2)
    if (slicedchosenImage == input) {
        blockInput = true;
        updateScore(1);
        console.log(`You were right! ${slicedchosenImage} was correct`);
        document.getElementById(input).style.backgroundColor = "green";
        setTimeout(changeImage, sleeptime);
    }   else {
        document.getElementById(input).style.backgroundColor = "red";
        updateScore("reset");
    }
}


// BUTTONS FUNKTION ZUWEISEN
for (let i = 0; i < buttonContainer.children.length; i++) {
    document.getElementById(buttonContainer.children[i].id).addEventListener("click", function () {buttonPressed(buttonContainer.children[i].id)});
}