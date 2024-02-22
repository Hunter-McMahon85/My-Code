const MMperInch = 25.4

function inchesToMM(inches) {
    return inches * MMperInch
}

function getPerimeter(width, height) {
    return (width * 2) + (height * 2);
}

function displayOutput(width, height) {
    let widthMM = inchesToMM(width);
    let heightMM = inchesToMM(height);
    let perimeterin = getPerimeter(width, height);
    let perimetermm = getPerimeter(widthMM, heightMM);
    console.log("For an", width, "x", height, "inch sheet of paper:");
    console.log("Perimeter =", perimeterin, "inches or", perimetermm, "millimeters");
}