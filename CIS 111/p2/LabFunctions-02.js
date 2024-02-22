/* 
  Name: Hunter McMahon
  Class: CIS 111
  Description: <This is lab 2, what else is there to it?>
*/
//arg
function doAlert(input) {
    alert(input)
}
//width height sum)squared
function getDiagonal(side1, side2) {
    let absqr = Math.pow(side1, 2) + Math.pow(side2, 2)
    let diagonal = Math.sqrt(absqr)
    return diagonal;
}
//arg square
function square_v1(input) {
    let answer = input * input;
    return answer;
}
//I think the string "4" worked because there was a number present that the console could identify, meanwhile the string "abc" did not contain any sort of number and therefore, no interger string could be identified and ran through the math.pow function (and if there was a number present in the letters, parsefloat would need to be used to find it) 
//arg
function square_v2(input) {
    let answer = input * input;
    console.log(typeof (input) + ",", answer);
}