document.getElementById("ButtonIntervalle").addEventListener("click", function () {MenubuttonPressed("intervalle/intervalle.html")});
document.getElementById("ButtonToene").addEventListener("click", function () {MenubuttonPressed("toene/toene.html")});

function MenubuttonPressed(x) {
    window.open(x, "_self")
}