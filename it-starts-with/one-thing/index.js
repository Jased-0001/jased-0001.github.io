window.addEventListener("load", function() {
    fetch('https://jased.xyz/it-starts-with/one-thing/lyrics.txt')
    .then(response=> response.text())
    .then(text=> document.getElementById('lyrics').innerHTML = text);
});