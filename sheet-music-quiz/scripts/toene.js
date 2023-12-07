// declarations
var buttonContainer = document.getElementById("button-container")
var settingsContainer = document.getElementById("settings");
var blockInput = false;
var lastchosenImage;
var images = [];
var settingsOptions = [];
var sleeptime = 500;    


// RANDOM IMAGE
var imagesViolin = [
    "0A2.png",
    "0H2.png",
    "0C3.png",
    "0D3.png",
    "0E3.png",
    "0F3.png",
    "0G3.png",
    "0A3.png",
    "0H3.png",
    "0C4.png",
    "0D4.png",
    "0E4.png",
    "0F4.png",
    "0G4.png",
    "0A4.png",
    "0H4.png",
    "0C5.png",
];
var imagesBass = [
    "1C1.png",
    "1D1.png",
    "1E1.png",
    "1F1.png",
    "1G1.png",
    "1A1.png",
    "1H1.png",
    "1C2.png",
    "1D2.png",
    "1E2.png",
    "1F2.png",
    "1G2.png",
    "1A2.png",
    "1H2.png",
    "1C3.png",
    "1D3.png",
]
var imagesViolinVorzeichen = [
];
var imagesBassVorzeichen = [
];
function changeImage() {
    // SETTINGS
    images = []
    settingsOptions = [];
    for (let i = 0; i < settingsContainer.children.length; i++) {
        if (settingsContainer.children[i].tagName != "INPUT") {
            continue;
        }
        settingsOptions = settingsOptions.concat(settingsContainer.children[i].checked);
        if (settingsOptions[0] == false && settingsOptions[1] == false) {
            settingsOptions[0] = true;
            settingsContainer.children[0].checked = true;
        }
    }
    console.log(settingsOptions);
    if (settingsOptions[0]) {
        images = images.concat(imagesViolin);
        if (settingsOptions[2]) {
            images = images.concat(imagesViolinVorzeichen);
        }
    }
    if (settingsOptions[1]) {
        images = images.concat(imagesBass)
        if (settingsOptions[2]) {
            images = images.concat(imagesBassVorzeichen)
        }
    }


    if (typeof slicedchosenImage != 'undefined') {
        document.getElementById(slicedchosenImage).style.backgroundColor = document.getElementById(slicedchosenImage).className; 
    }
    blockInput = false;
    chosenImage = images[Math.floor(Math.random() * images.length)];
    document.getElementById("change-img").src = `../images/toene/${chosenImage}`;
    if (chosenImage == lastchosenImage) {
        changeImage()
    }   else {
        resetColor();
        lastchosenImage = chosenImage;
    }
}
changeImage()

// resetColor
function resetColor() {
    for (let i = 0; i < buttonContainer.children.length; i++) {
        document.getElementById(buttonContainer.children[i].id).style.backgroundColor = document.getElementById(buttonContainer.children[i].id).className; 
    }
}


// buttonpressed
function buttonPressed(input) {
    if (blockInput) {
        console.log("WAIT FFS")
        return;
    }
    slicedchosenImage = chosenImage.replace(".png", "").slice(1,-1)
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


// make buttons work
for (let i = 0; i < buttonContainer.children.length; i++) {
    document.getElementById(buttonContainer.children[i].id).addEventListener("click", function () {buttonPressed(buttonContainer.children[i].id)});
}

// Allow Keyboard inputs 
document.addEventListener("keypress", function(event) {
    keyboardinput = event.key.toLowerCase()
    console.log(keyboardinput);
    const keyMappings = {
        y: "C",
        x: "D",
        c: "E",
        v: "F",
        b: "G",
        n: "A",
        m: "H"
      };
      if (keyboardinput in keyMappings) {
        buttonPressed(keyMappings[keyboardinput]);
      }
})