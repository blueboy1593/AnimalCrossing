<template>
  <div class="logoImage">
    <div class="logoImg">
      <router-link to="/">
        <img src="../assets/images/logo.png" alt="" />
      </router-link>
    </div>
  </div>
</template>

<script></script>

<style scoped>
* {
  background-image: none;
  background-size: cover;
  z-index: 999;
}

.logoImage {
  margin-top: 1%;
  margin-left: 4%;
  margin-bottom: -6%;
  background-image: none;
  grid-area: logoImage;
  display: grid;
  }

.logoImg {
  width: 10%;
  display: inline-block;
  /* background-color: red; */
}

.logoImg img {
  width: 100%;
}
</style>
