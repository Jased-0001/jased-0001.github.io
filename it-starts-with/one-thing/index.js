window.addEventListener("load", function() {
    var parsedlyrics;

    fetch('https://jased.xyz/it-starts-with/one-thing/lyrics.txt')
    .then(response => response.text())
    .then(text => document.getElementById("lyrics").innerHTML = text.replace(/(?:\r\n|\r|\n)/g, "<br>"))
    .catch(error => console.error(error))

    var lyricz = parsedlyrics
});