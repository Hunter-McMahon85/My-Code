/* 
  Name: Hunter McMahon
  Class: CIS 111
  Description: <this is catalog for project 3>
*/
//step 3 

function padString(data, maxLength, padCharacter, padLeft) {
    switch (padLeft) {
        case true:
            return data.padStart(maxLength, padCharacter)
        case false:
            return data.padEnd(maxLength, padCharacter)
        default: console.log(" please enter a boolean for padleft")
    }
    //padStart and padEnd automatically put padding in
}

//step 6
//songs were chosen randomly from the same week chosen by a random date generator 
const songs = [
    {
        title: "Skeletons",
        artist: "Stevie Wonder",
        position: 21,
        weeksOnChart: 9
    },
    {
        title: "Faith",
        artist: "George Michael",
        position: 1,
        weeksOnChart: 8
    },
    {
        title: "The One I Love",
        artist: "R.E.M",
        position: 12,
        weeksOnChart: 13
    },
    {
        title: "Bad",
        artist: "Michael Jackson",
        position: 71,
        weeksOnChart: 13
    },
    {
        title: "U Got The Look",
        artist: "Prince",
        position: 65,
        weeksOnChart: 20
    }
]
//step 7 basically the declaration of thou methhods
let catalogObject = {
    _songs: [],

    weektxt: "Weeks On Chart",

    addSong: function addSong(props) {
        for (var i = 0; i < songs.length; i++) {
            this._songs.push(songs[i]);
        }
        for (var i = 0; i < songs.length; i++) {
            this._songs[i].title.trim();
        };

        // this._songs.unshift({ title: "title", artist: "Artist", position: "Position", })
    },

    listSongs: function out() {
        let MaxL = this._maxTitleLength();
        let MaxA = this._maxArtistLength();
        let MaxP = this._maxPositionLength();
        let MaxW = this._maxWeeksOnChartLength();
        console.log(`${this.pad("position", MaxP, " ", false)} ${this.pad("Title", MaxL, " ", false)} ${this.pad("Artist", MaxA, " ", false)} ${this.pad("Weeks on Chart", MaxW, " ", false)}`)
        for (var i = 0; i < songs.length; i++) {
            let position = this._songs[i].position.toString();
            let title = this._songs[i].title;
            let artist = this._songs[i].artist;
            let weeks = this.weektxt + ' ' + this._songs[i].weeksOnChart.toString();
            let p = this.pad(position, MaxP, " ", false);
            let t = this.pad(title, MaxL, " ", false);
            let a = this.pad(artist, MaxA, " ", false);
            let w = this.pad(weeks, MaxW, " ", false);
            console.log(`${p} ${t} ${a} ${w}`);
            //the position etc. is defined as a local variable and thus objects must be assigned to them
        }
    },
    //part 8

    pad: function padString(data, maxLength, padCharacter, padLeft) {
        switch (padLeft) {
            case true:
                return data.padStart(maxLength, padCharacter)
            case false:
                return data.padEnd(maxLength, padCharacter)
        }
    },

    _maxTitleLength: function maxttlength() {
        let maxtl = 0;
        for (let i = 0; i < this._songs.length; i++) {
            if (this._songs[i].title.length > maxtl) {
                maxtl = this._songs[i].title.length;
            };
        };
        return maxtl
    },
    _maxArtistLength: function maxtalength() {
        let maxa = 0;
        for (let i = 0; i < this._songs.length; i++) {
            if (this._songs[i].artist.length > maxa) {
                maxa = this._songs[i].artist.length;
            };
        };
        return maxa
    },
    _maxPositionLength: function maxtplength() {
        let maxp = 0;
        let post = "position"

        for (let i = 0; i < this._songs.length; i++) {
            let pos = this._songs[i].position.toString()
            if (pos.length > post.length) {
                let diff = pos.length - post.length;
                maxp = diff + post.length;
            } else {
                maxp = post.length;

            };
        };
        return maxp
    },

    _maxWeeksOnChartLength: function maxtoclength() {
        let maxoc = 0;
        for (let i = 0; i < this._songs.length; i++) {
            let oc = this._songs[i].position.toString();
            let leng = oc.length + this.weektxt.length
            if (leng > maxoc) {
                maxoc = leng;
            };
        };
        return maxoc.parseint
    },
}

const catalog = Object.create(catalogObject);
