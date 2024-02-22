const MMperInch = 25.4

function inchesToMM(inches) {
    return inches * MMperInch
}

function displayOutput() {
    let widthMM = inchesToMM(8.5);
    let lengthMM = inchesToMM(11);
    console.log("8.5 x 11 inches=", widthMM, "x", lengthMM, "millimeters");
}