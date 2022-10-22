var tag = document.createElement('script');

tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

var player;
function onYouTubeIframeAPIReady() {
  player = new YT.Player('player', {
    videoId: 'FLDqgCwv91I',
    playerVars: {
      'playsinline': 1,
      'cc_load_policy': 1,
      'controls': 0,
      'vq': '144p',
      'autoplay': 1,
      'mute': 1
    },
    events: {
      'onReady': onPlayerReady,
      'onStateChange': checkDidEnd
    }
  });
}

function checkDidEnd() {
    if (player.getPlayerState() == 0) {
        window.location.href = "about://blank";
    }
}

// 4. The API will call this function when the video player is ready.
function onPlayerReady(event) {
    event.target.playVideo();

    var w = window.innerWidth;
    var h = window.innerHeight;

    player.width = w;
    player.height = h;
}

document.addEventListener("click", function() {
    player.unMute()
});