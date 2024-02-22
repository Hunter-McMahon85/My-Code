/*
  Name: Hunter McMahon
  Class: CIS 111
  Description: <lab 09s js file, why the zero if there is only 9 of them>
*/

//store phonetic values in a JSON object
//jsone can take functions
const natophone = {
    'a': 'Alpha',
    'b': 'Bravo',
    'c': 'Charlie',
    'd': 'Delta',
    'e': 'Echo',
    'f': 'Foxtrot',
    'g': 'Golf',
    'h': 'Hotel',
    'i': 'India',
    'j': 'Juliet',
    'k': 'Kilo',
    'l': 'Lima',
    'm': 'Mike',
    'n': 'November',
    'o': 'Oscar',
    'p': 'Papa',
    'q': 'Quebec',
    'r': 'Romeo',
    's': 'Sierra',
    't': 'Tango',
    'u': 'Uniform',
    'v': 'Victor',
    'w': 'Whiskey',
    'x': 'Xray',
    'y': 'Yankee',
    'z': 'Zulu',
    '0': 'Zero',
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five',
    '6': 'Six',
    '7': 'Seven',
    '8': 'Eight',
    '9': 'Nine',
};

//the dirty work
//converts letter based on JSON list
function chToNATO(ch) {
    ch = ch.toLowerCase();
    if (natophone[ch] != undefined) {
        return natophone[ch];
    } else {
        return ch;
    }
}

function wordToNATO(word) {
    let outputw = "";
    //dirty work of the conversion
    for (let i = 0; i < word.length; i++) {
        let con = chToNATO(word.charAt(i))
        outputw += con + ' ';
    }
    return outputw
}

function sentenceToNATO(sentence) {
    let sout = "";
    let words = sentence.split();

    for (let i = 0; i < words.length; i++) {
        let converse = wordToNATO(words[i]);
        sout += converse + '';
    }
    return sout
}

function takeinput(evt) {
    const data = document.querySelector('#rawinput').value.trim();
    let convert = sentenceToNATO(data);
    let display = document.querySelector('#output')
    display.innerHTML = convert;

}
document.querySelector("#verbalize").addEventListener('click', takeinput)