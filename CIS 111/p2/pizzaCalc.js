/* 
  Name: Hunter McMahon
  Class: CIS 111
  Description: <This is the js 4 the PIZZA CALCULATOR!!!! *echos*>
*/
let costin = prompt("enter the cost of the pizza:");
let diameterin = prompt("enter the diameter (in inches) of the pizza:");
let cost = parseFloat(costin);
let diameter = parseFloat(diameterin);
function pizzaPSI(cost, diameter) {
  let radius = diameter / 2;
  let area = Math.PI * Math.pow(radius, 2);
  let psi = cost / area;
  return psi
}

// display to pizzacalc.html,
let Element = document.querySelector("div")
let text = "Hit Reload/Refresh to run again." + "<br>" + "Cost: $" + cost + "<br>" + "Diameter: " + diameter + "<br>" + "Cost PSI: " + pizzaPSI(cost, diameter)
Element.innerHTML = text