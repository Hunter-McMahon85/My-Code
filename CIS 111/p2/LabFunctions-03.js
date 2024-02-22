/* 
  Name: Hunter McMahon
  Class: CIS 111
  Description: This is the JS file for lab 3
*/
function sumOddInts(n) {
  if (n < 0) {
    return 0;
  }
  let sumodd = 0;
  for (let i = 1; i <= n; i = i + 2) {
    sumodd = sumodd + i
  }

  return sumodd
}
let number_string = prompt("enter a positive number: ");
let number = parseInt(number_string);

let sum_1_n = sumOddInts(number)

//inserting text to html (uses css selector syntax)
let element = document.querySelector("div")
let text = "the sum of all odd numbers from 1 to " + number_string + " is " + sum_1_n
element.innerHTML = text 