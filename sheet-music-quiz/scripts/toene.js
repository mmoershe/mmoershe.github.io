// declarations
var buttonContainer = document.getElementById("button-container")
var settingsContainer = document.getElementById("settings");
var blockInput = false;
var lastchosenImage;
var images = [];
var settingsOptions = [];
var sleeptime = 500;    


// RANDOM IMAGE
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
    document.getElementById("change-img").src = `../toene/images/${chosenImage}`;
    if (chosenImage == lastchosenImage) {
        console.log("doing it again.")
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
    console.log(`Buttonpressed = ${input}`)
    if (blockInput) {
        console.log("WAIT FFS")
        return;
    }
    slicedchosenImage = chosenImage.split("/")
    slicedchosenImage = slicedchosenImage[slicedchosenImage.length - 1].replace(".png", "").replace("'", "").replace("'", "").replace("'", "").replace(",", "").replace(",", "").replace("0", "").toUpperCase()
    slicedchosenImage = convert_key(slicedchosenImage)
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
    console.log(`slicedchosenImage = ${slicedchosenImage}`)
}
function convert_key(input) {
    switch(input) {
        default: 
            return input
        case "BS":
            return "C"
        case "CF":
            return "B"
        case "ES":
            return "F"
        case "FF": 
            return "E"
        case "DF":
            return "CS"
        case "EF":
            return "DS"
        case "GF":
            return "FS"
        case "AF":
            return "GS"
        case "BF":
            return "AS"
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
        s: "CS",
        x: "D",
        d: "DS",
        c: "E",
        v: "F",
        g: "FS",
        b: "G",
        h: "GS",
        n: "A",
        j: "AS",
        m: "B"
      };
      if (keyboardinput in keyMappings) {
        buttonPressed(keyMappings[keyboardinput]);
      }
})


