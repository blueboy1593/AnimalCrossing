<template>
  <div class="music">
    <div class="player">
      <div class="album">
        <img src="../../src/assets/images/navi.png" class="albumImg" alt="" />
      </div>
      <div class="controls">
        <!-- ♪ -->
      </div>
    </div>
  </div>
</template>

<script></script>

<style scoped>
.music {
  /* display: block; */
  /* display: grid; */
  /* grid-area: music; */
  width: 8%;
  height: 8%;
  overflow: hidden;
  border-radius: 10px;
  position: fixed;
  right: 18%;
  top: 4%;
  background-color: rgba(36, 116, 136, 0.356);
}

.player {
  border-radius: 10px;
  /* transform: scale(0.1); */
}

.album {
  border-radius: 50%;
}

.albumImg {
  transform: scale(0.1);
  transform-origin: 0 0;
  border-radius: 50%;
  margin-top: 5%;
  margin-left: 3%;
}

.controls {
}
</style>
