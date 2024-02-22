/* 
  Name: Hunter McMahon
  Class: CIS 111
  Description: <want to see a majoc trick? jk this is just project 4 lol get rekt>
*/

const cardnum = "A234567890JQK"
const suit = "CDHS"

const cardObject = {
    /*
       TODO [C]: Add the following properties (remember to start properties with an underscore):
       - timer ID property used to stop timer, initialized to null, example:
       _intervalID: null,
       - initial counter property starting value
       - counter property that will count down to zero
    */
    _cards: cardnum.split(""),
    _suits: suit.split(""),
    _startcount: null,
    _counter: null,
    _intervalID: null,
    getRandomCard: function () {
        let rancar = this._cards[this.getRandomNumber(0, 13)];
        if (rancar === "0") {
            rancar = "10";
        };
        return rancar
        // Returns a random card value from the cards array 0 = 10 
    },
    getRandomSuit: function () {
        return this._suits[this.getRandomNumber(0, 4)]
        // Returns a random suit value from the suits array via a random array index value for the suits array
    },

    loadImages: function () {
        document.querySelector("#card").src = `cards/${this.getRandomCard()}${this.getRandomSuit()}.png`;
        // Updates the img element src attribute with a randomly generated card and suit image file name by calling getRandomCard() and getRandomSuit() to create image filename
    },

    countDown: function () {
        if (this._counter > 0) {
            this._counter--;
            this.displayCountDown();
        }
        if (this._counter <= 0) {
            this.stopCountDownTimer();
            this.loadImages();
        }
        // Decrements and displays the count down value, and upon reaching 0 stops timer and displays the card image
    },

    displayCountDown: function () {
        if (this._counter >= 0) {
            document.querySelector("#countDownSpan").textContent = `${this._counter}`;
        }
        //Updatea countdown span element with current countdown value via a reference to countdown span and set the span textContent property with _counter
    },

    startCountDownTimer: function (start) {
        // sets values of objects
        this._startCount = start;
        this._counter = this._startCount;
        this.displayCountDown();
        this._intervalID = setInterval(this.countDown.bind(this), 1000);
    },

    stopCountDownTimer: function () {
        clearInterval(this._intervalID)
        //Stops timer
    },

    getRandomNumber: function (min, max) {
        // Generates a random integer between min (included) and max (excluded)
        let randomNum = Math.random() * (max - min) + min;
        return Math.floor(randomNum);
    }
}
const timedCard = Object.create(cardObject);
timedCard.startCountDownTimer(5);