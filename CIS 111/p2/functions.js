/* 
  Name: Hunter McMahon
  Class: CIS 111
  Description: This is the JS file for STEP 3 of project 2
*/
//parta.
function avg3(uno, dos, tres) {
    let total = uno + dos + tres;
    let ave = total / 3;
    return ave
}
//partb.
function getTip(cost, percenttip) {
    let tip = cost * percenttip;
    return tip
}
//part.c
function pizzaPSI(cost, diameter) {
    let radius = diameter / 2;
    let area = Math.PI * Math.pow(radius, 2);
    let psi = cost / area;
    return psi
}
//partd.
/*here I used a regular expression,
all of the work is done by the let result = section of the code
basically a regular expresion is just a defined patern thats used to match/test for/find character combos in strings
so what needs to be done first is we need to define what character we are looking for in a string which we do within 2 forward slashes 
to do this there are a few classes of special character that can be used
in our case we only need to use characters/syntax from two of these classes (an assertion and a group/range)
the assertion in this case is the ^ character which basically says that we want to match the 1st character of our string to any one of our defined characters in the regular expresion
Then to define a character set we have to put the characters of our set within brackets [],
in the bracket,s we can either list our the desired set character by character or define a range of letters and numbers by puting a hyphen - in between the start and end values
(letters and numbers in order, capital and lower case are considered different so since we want both upper and lower case letters we define the character set as the whole alphabet for both with the notation a-zA-Z)
we can then use the .test() methhod to see if our string matches any one of the characters within the defined character set in our regular expression.
if the entry string character matches with one within the defined character set, then .test() will give the value true, if not then it will give a value of false. 
that value can be then assigned to a variable which i can then just have the function return.
 */
function isAlpha(entry) {
    let result = /^[a-zA-Z]/.test(entry);
    return result
}
//part e.
function sumNumbers(num) {
    if (num < 0) {
        let sumneg = 0;
        for (let i = 0; i >= num; i--) {
            sumneg = sumneg + i
        }
        return sumneg
    }
    else {
        let sumpos = 0;
        for (let i = 0; i <= num; i++) {
            sumpos = sumpos + i
        }
        return sumpos
    }
}
