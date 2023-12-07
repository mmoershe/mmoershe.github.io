// SCORE STUFF
var score = 0;
var highscore = 0;
function updateScore(x) {
    if (x == "reset") {
        if (score > highscore) {
            highscore = score;
        }
        score = 0;
    }   else {
        score += parseInt(x);
    }
    document.getElementById("score").innerHTML = `${score} I ${highscore}`;
}