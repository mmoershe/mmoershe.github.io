  // Enable WEBMIDI.js and trigger the onEnabled() function when ready
  WebMidi
    .enable()
    .then(onEnabled)
    .catch(err => console.log(err));

  // Function triggered when WEBMIDI.js is ready
  function onEnabled() {

    // Display available MIDI input devices
    if (WebMidi.inputs.length < 1) {
      console.log("No device detected.");
    } else {
      WebMidi.inputs.forEach((device, index) => {
        console.log(`${index}: ${device.name}`);
      });
    }
    const mySynth = WebMidi.inputs[0];
    // const mySynth = WebMidi.getInputByName("TYPE NAME HERE!")
  
    mySynth.channels[1].addListener("noteon", e => {
    console.log(`MIDI INPUT: ${e.note.name}`);
    if (e.note.name == "B") {
        buttonPressed("H");
        return;
    }
    buttonPressed(e.note.name)
  });
}

  