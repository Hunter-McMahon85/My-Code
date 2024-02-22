/*
  Name: Hunter McMahon
  Class: CIS 111
  Description: <the code of p5... the end is near>
*/

//our global variables

const words = wordList;
let guesses = [];
let word = "";
let sansunderarray = [];
//the dirty work

function handleGuessButtonClick() {
    //getting the guess
    let inguess = document.querySelector('#inputguess').value.trim();
    let guessup = inguess.toUpperCase();
    let guess = guessup.charAt(0);
    //testing for duplicate guesses and storing them to the guesses array
    if (guesses.indexOf(guess) < 0) {
        guesses.push(guess);
    }
    //clear the input box
    document.querySelector("#inputguess").value = '';

    //update the blank underscores
    displayWordUnderscores();
    displayGuessedLetters();
};

function handleStartRestartButtonClick() {
    //change button text
    document.querySelector('#reset').textContent = 'Restart';
    //reseting the puzzle 
    guesses.splice(0, guesses.length);
    sansunderarray.splice(0, sansunderarray.length);
    word = words[getRandomNumber(0, 51)].toUpperCase();
    displayGuessedLetters();
    displayWordUnderscores();
};

function displayGuessedLetters() {
    document.querySelector("div").innerHTML = guesses.join("<br>");
}

function displayWordUnderscores() {
    //sansunderarry holds underscores and correctly guessed letters and is whats displayed
    let wordray = word.split('');
    let guesslen = guesses.length - 1;
    let wordindex = wordray.indexOf(guesses[guesslen]);
    let matchedletters = [];
    //puts underscores into empty array corresponding to the word
    if (sansunderarray.length <= 1) {
        for (let i = 0; i < wordray.length; i++) {
            sansunderarray.push("_");
        }
    };
    //updates the "blanks" with each letter
    if (sansunderarray.length > 1) {
        if (wordindex != -1) {
            // check to see if letter appears multiple times 
            for (let i = 0; i < wordray.length; i++) {
                if (wordray[i] === guesses[guesslen]) {
                    matchedletters.push(i);
                }
                //update the word
                for (let i = 0; i < matchedletters.length; i++) {
                    let appears = matchedletters[i];
                    sansunderarray.splice(appears, 1, wordray[appears]);
                };
            };
        };
        document.querySelector("span").innerHTML = sansunderarray.join(' ');
    };
};

function getRandomNumber(min, max) {
    // Generate a random integer between min (included) and max (excluded)
    let randomNum = Math.random() * (max - min) + min;
    return Math.floor(randomNum);
};;
//Calling our functions for the dirty work based on which buttons clicked

document.querySelector("#guess").addEventListener("click", handleGuessButtonClick);
document.querySelector("#reset").addEventListener("click", handleStartRestartButtonClick);