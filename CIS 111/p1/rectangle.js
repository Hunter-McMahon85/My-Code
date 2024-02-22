let winput = prompt("enter a width in inches")
let hinput = prompt("enter a height in inches")
let width = parseFloat(winput)
let height = parseFloat(hinput)

function getPerimeter(width, height) {
    return (width * 2) + (height * 2);
}
function getArea(width, height) {
    return width * height;
}
function displayOutput(width, height) {
    let perimeterin = getPerimeter(width, height);
    let areain = getArea(width, height);
    console.log("width =", width,);
    console.log("height =", height);
    console.log("area =", areain);
    console.log("perimeter =", perimeterin);
}



