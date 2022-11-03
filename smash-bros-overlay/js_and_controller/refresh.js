
function reload(){
    document.getElementById("player1").innerHTML = localStorage.getItem("lt");
    document.getElementById("player2").innerHTML = localStorage.getItem("rt");
    document.getElementById("round").innerHTML = localStorage.getItem("rnd");
    document.getElementById("score1").innerHTML = localStorage.getItem("ls");
    document.getElementById("score2").innerHTML = localStorage.getItem("rs");
    document.getElementById("p1char").src = localStorage.getItem("li");
    document.getElementById("p2char").src = localStorage.getItem("ri");
}; setInterval('reload()', 1);
