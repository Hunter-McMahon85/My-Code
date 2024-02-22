/* 
  Name: Hunter McMahon
  Class: CIS 111
  Description: <this is array object for the week 5 lab>
*/
/*
    The array object includes a sort() method to sort the array items
    The sort uses the ASCII table (http://www.asciitable.com/) 
    numerical equivalent of a character to determine the sort order,
    which means uppercase letters sort before lowercase letters.
*/

/*
    Work with string array of animals
*/
const AnimalArray = ['dog', 'cat', 'wolf', 'bear', 'bird'];
console.log("** Animal Array **");
console.log(AnimalArray);
console.log(AnimalArray.sort());

/*
    Work with string array of animals of mixed case
*/
function compareStringMixedCase(a, b) {
    // Compare two strings, converting to uppercase first
    const aUpper = a.toUpperCase();
    const bUpper = b.toUpperCase();
    if (aUpper > bUpper) {
        return 1;
    } else if (aUpper < bUpper) {
        return -1;
    } else {
        return 0;
    }
    // Above conditional condensed using ternary syntax
    // return aUpper == bUpper ? 0 : aUpper > bUpper ? 1 : -1;
}

const AnimalArrayMixedCase = ['Dog', 'cat', 'Wolf', 'Bear', 'bird'];
console.log("** Animal Array Mixed Case **");
console.log(AnimalArrayMixedCase);
console.log(AnimalArrayMixedCase.sort());
console.log(AnimalArrayMixedCase.sort(compareStringMixedCase));

/*
    Work with number array
*/
const NumberArray = []; // Empty array
const NumberMin = 1;    // Minimum random number
const NumberMax = 100;  // Maximum random number
const NumberCount = 20; // Array element count

function getRandomNumber(min, max) {
    // Generate a random integer between min (included) and max (excluded)
    let randomNum = Math.random() * (max - min) + min;
    return Math.floor(randomNum);
}

// Populate array with random numbers
for (let i = 0; i < NumberCount; i++) {
    const randomNumber = getRandomNumber(NumberMin, NumberMax);
    NumberArray.push(randomNumber);
}

function compareNumbers(a, b) {
    // Compare two numbers for array sort() method
    if (a > b) {
        return 1;
    } else if (a < b) {
        return -1;
    } else {
        return 0;
    }
}

// Output original and sorted array
// Note that the "sorted" array is not always accurately sorted
console.log("** Number Array **");
console.log(NumberArray);
console.log(NumberArray.sort());
console.log(NumberArray.sort(compareNumbers));

/*
    Work with array of objects
*/
function comparePerson(a, b) {
    // Compare two people name properties for array sort() method
    const aUpper = a.name;
    const bUpper = b.name;
    if (aUpper > bUpper) {
        return 1;
    } else if (aUpper < bUpper) {
        return -1;
    } else {
        return 0;
    }
}
const PeopleArray = [
    {
        name: "Sadie",
        age: 22
    },
    {
        name: "Chloe",
        age: 31
    },
    {
        name: "Elara",
        age: 35
    },

];
console.log("** Object Array People **");
console.log(PeopleArray);
console.log(PeopleArray.sort());
console.log(PeopleArray.sort(comparePerson));

//errors found/corrected 2/3