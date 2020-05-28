<template>
  <div class="infoCard">
    <div class="photo">
      <!-- <img src="../../assets/images/fish.png" height="100%" class="photoImg" alt=""> -->
      <img :src="infoCard.src" class="image" />
    </div>
    <div class="infoName">
      {{ infoCard.name }}
    </div>
    <div class="infoDetail">
      {{ infoCard.price }}
    </div>
  </div>
</template>

<script>
export default {
  name: "infoCard",
  props: ["infoCard"]
};
</script>

<style>
.infoCard {
  margin-top: 0.3rem;
  width: 120px;
  height: 150px;
  border-radius: 15px;
  background-color: #c1d2e1;
  overflow: hidden;
}

.infoCard:hover {
  transform: scale(1.02);
  opacity: 0.9;
  border: 3px solid #276dd68e;
}

.photo {
  width: 120px;
  height: 100px;
  border-radius: 15px;
  background-color: #aac8e4;
  text-align: center;
  overflow: hidden;
}

.image {
  height: 100px;
  /* display: block; */
  margin: 0 auto;
}

.infoName {
  text-align: center;
  font-weight: bolder;
  font-size: 1.1rem;
}

.infoDetail {
  text-align: center;
  font-weight: 100;
}
</style>
