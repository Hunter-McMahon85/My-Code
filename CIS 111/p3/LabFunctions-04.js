/* 
  Name: Hunter McMahon
  Class: CIS 111
  Description: <This is lab 4, LETS GET THIS BIT>
*/
//is alpha from proj 2
function isAlpha(entry) {
    let result = /^[a-zA-Z]/.test(entry);
    return result
}
//part 2

/*
for loop needs 
iterator: variable i; uses index of charecter here
initial value of iterator: i=0
stop condition: i =, i< or i<= string length in this case 
increment  i= i+1 or i++
update rules ie letter updates counter value else discard.
*/

function countLetters(strinput) {
    //stores # of letters
    let count = 0;

    //loop
    for (let i = 0; i < strinput.length; i++) {
        let charatindexi = strinput.charAt(i);
        if (isAlpha(charatindexi)) {
            count = count + 1
        }
    }
    return count;
}


// while loop version
function countLettersWhile(strinput) {
    let count = 0;

    //initialize iteratior beforehand
    let i = 0
    // while(stoping condition){ update rules and increment}
    while (i < strinput.length) {
        let charatindexi = strinput.charAt(i);
        if (isAlpha(charatindexi)) {
            count = count + 1;
        }
        i = i + 1;
    }

    return count;
}

//do while loop version

function countLettersdoWhile(strinput) {
    let count = 0;
    let i = 0;
    do {
        let charatindexi = strinput.charAt(i);
        if (isAlpha(charatindexi)) {
            count = count + 1
        }
        i++;
    } while (i < strinput.length);
    return count;
}

//part3

function countOccurrences(input, letter) {
    let count = 0;
    for (i = 0; i < input.length; i++) {
        if (input.charAt(i) == letter) {
            count++;
        }
    }
    return count;
}


//part4 closures 
//closures preserve variables values by means of the inter function staying alive- closures only work with functions 
let likes = 0
function handlelikepost() {
    let likes = 0;
    function addlike() {
        likes += 1;
        return likes
    }
}

const like = handleLikePost(1);
const doubleLike = handleLikePost(2);
