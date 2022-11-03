/*
SSBU basic HTML controller,
Made by Hunter McMahon to be Used by the UO smash bros club for
the streams of the duck hunt tournaments, if you happen to come 
accross this code be welcome to modify it to your needs. 
*/

let right_tag = "";
let left_tag = "";

let right_score = 0;
let left_score = 0;

let round = "";

let left_icon = "";
let right_icon = "";

localStorage.setItem("rt", right_tag);
localStorage.setItem("lt", left_tag);
localStorage.setItem("rs", right_score);
localStorage.setItem("ls", left_score);
localStorage.setItem("rnd", round);
localStorage.setItem("ri", right_icon);
localStorage.setItem("li", left_icon);

function set_right_tag() {
    //getting the right player tag
    right_tag = document.querySelector('#righttag').value.trim();
    localStorage.setItem("rt", right_tag);
    //clear the input box
    document.querySelector("#righttag").value = '';
};

function set_left_tag() {
    //getting the left player tag
    left_tag = document.querySelector('#leftttag').value.trim();
    localStorage.setItem("lt", left_tag);
    //clear the input box
    document.querySelector("#leftttag").value = '';
};

function set_tags() {
    //sets both of the tags
    set_right_tag()
    set_left_tag()
};

function set_round() {
    //getting the round
    round = document.querySelector('#round').value.trim();
    localStorage.setItem("rnd", round);

    //clear the input box
    document.querySelector("#round").value = '';
};

function set_left_icon() {
    //getting the left icon name
    left_icon = "char_icons/" + document.querySelector('#leftchar').value.trim() + ".png";
    localStorage.setItem("li", left_icon);
    //clear the input box
    document.querySelector("#leftchar").value = '';
};

function set_right_icon() {
    //getting the right icon name
    right_icon = "char_icons/" + document.querySelector('#rightchar').value.trim() + ".png";
    localStorage.setItem("ri", right_icon);
    //clear the input box
    document.querySelector("#rightchar").value = '';
};

function set_icons() {
    // sets both icons at the same time
    set_left_icon();
    set_right_icon();
};


function score_r() {
    // increments right players score
    right_score += 1;
    localStorage.setItem("rs", right_score);
};

function score_l() {
    // increments the left players score
    left_score += 1;
    localStorage.setItem("ls", left_score);
};

function reset_score() {
    // resets all points to 0
    right_score = 0;
    left_score = 0;
    localStorage.setItem("rs", right_score);
    localStorage.setItem("ls", left_score);
};

function reset_tag() {
    // removes both tags
    right_tag = "";
    left_tag = "";
    localStorage.setItem("rt", right_tag);
    localStorage.setItem("lt", left_tag);
};

function reset_icon() {
    // resets the icons to default
    right_icon = "";
    left_icon = "";
    localStorage.setItem("ri", right_icon);
    localStorage.setItem("li", left_icon);
};

function reset_all() {
    // resets all attributes
    reset_icon()
    reset_score()
    reset_tag()
    round = "";
    localStorage.setItem("rnd", round);
};

document.querySelector("#tags").addEventListener("click", set_tags);
document.querySelector("#eltag").addEventListener("click", set_left_tag);
document.querySelector("#ertag").addEventListener("click", set_right_tag);
document.querySelector("#iconbut").addEventListener("click", set_icons);
document.querySelector("#elib").addEventListener("click", set_left_icon);
document.querySelector("#erib").addEventListener("click", set_right_icon);
document.querySelector("#subround").addEventListener("click", set_round);
document.querySelector("#winL").addEventListener("click", score_l);
document.querySelector("#winR").addEventListener("click", score_r);
document.querySelector("#resetscore").addEventListener("click", reset_score);
document.querySelector("#resettag").addEventListener("click", reset_tag);
document.querySelector("#reseticon").addEventListener("click", reset_icon);
document.querySelector("#resetall").addEventListener("click", reset_all);