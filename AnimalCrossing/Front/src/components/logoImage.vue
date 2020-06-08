<template>
  <div class="logoImage">
    <div class="logoImg">
      <router-link to="/">
        <img src="../assets/images/logo.png" alt="" />
      </router-link>
    </div>
    <span>
      <img class="mdmd" src="../assets/images/mdmd.png" alt="" />
      <!-- <img class="mdmd" src="../assets/images/mdmd1.png" alt=""> -->
    </span>
    <p class="pinkBubble">모두 함께 즐기는 모여봐요 동물의 숲</p>
  </div>
</template>

<script></script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Jua&display=swap");

* {
  background-image: none;
  background-size: cover;
  z-index: 2;
  font-family: "Jua", sans-serif;
  color: #e9f8f6;
}

.logoImage {
  margin-top: 1%;
  margin-left: 4%;
  margin-bottom: -6%;
  background-image: none;
  grid-area: logoImage;

  /* display: grid; */
}

.logoImg {
  width: 10%;
  display: inline-block;
  /* background-color: red; */
}

.logoImg img {
  width: 100%;
}

.mdmd {
  margin-bottom: 21px;
  margin-left: 18px;
  width: 100px;
  height: 40px;
}

.pinkBubble {
  display: none;
  position: absolute;
  /* width: 50px; */
  padding: 5px;
  -webkit-border-radius: 8px;
  -moz-border-radius: 8px;
  border-radius: 8px;
  /* background: rgba(233, 97, 154, 0.315); */
  background: #0e433a8e;
  font-size: 14px;
  text-align: center;
  margin-top: -100px;
  margin-left: 130px;
  /* margin-left: 10px; */
}

.pinkBubble:after {
  position: absolute;
  bottom: -100%;
  right: 50%;
  border: solid transparent;
  border-bottom-color: rgba(233, 97, 154, 0.315);
  border-width: 4px;
  content: " ";
}

span:hover + p.pinkBubble {
  display: block;
}
</style>
