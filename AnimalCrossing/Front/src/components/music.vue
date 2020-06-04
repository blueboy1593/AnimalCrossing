<template>
  <!-- <div class="player"> -->
  <!-- <div class="album">
        <img src="../../src/assets/images/navi.png" class="albumImg" alt="" />
  </div>-->
  <!-- <audio src="../../src/assets/audios/navi.mp3" class="audioCon" loop autoplay></audio> -->
  <audio controls autoplay class="player">
    <source src="../../src/assets/audios/navi.mp3" type="audio/mpeg" />
  </audio>
  <!-- </div> -->
</template>

<script></script>

<style scoped>
.player {
  /* display: grid; */
  /* grid-area: music; */
  width: 16%;
  height: 8%;
  /* overflow: hidden; */
  /* border-radius: 10px; */
  position: fixed;
  right: 16%;
  z-index: 3;
  top: 4%;
  opacity: 0.5;
  /* background-color: rgba(36, 116, 136, 0.356); */
  /* border-radius: 10px; */
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
