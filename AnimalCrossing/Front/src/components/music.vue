<template>
  <audio controls volume="0.1" autoplay preload class="player">
    <source src="../../src/assets/audios/navi.mp3" type="audio/mpeg" />
  </audio>
</template>

<script></script>

<style scoped>
.player {
  width: 16%;
  height: 8%;
  position: fixed;
  right: 16%;
  z-index: 3;
  top: 4%;
  opacity: 0.5;
}

.player:focus {
  outline: none;
}

.album {
  height: 100%;
  border-radius: 50%;
}

.albumImg {
  transform: scale(0.1);
  transform-origin: 0 0;
  border-radius: 50%;
  margin-top: 5%;
  margin-left: 3%;
}

.audioCon {
  width: 100%;
}
</style>
