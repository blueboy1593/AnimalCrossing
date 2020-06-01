<template>
  <div class="infoCard">
    <div class="photo">
      <!-- <img src="../../assets/images/fish.png" height="100%" class="photoImg" alt=""> -->
      <img
        v-if="routePath === '/info/neighbor'"
        :src="getAnimalImgPath(infoCard.engname)"
        class="image"
      />
      <img
        v-if="routePath === '/info/fish'"
        :src="getFishImgPath(infoCard.name)"
        class="image"
      />
      <img
        v-if="routePath === '/info/insect'"
        :src="getInsectImgPath(infoCard.name)"
        class="image"
      />
      <img
        v-if="routePath === '/info/fossil'"
        :src="getFossilImgPath()"
        class="image"
      />
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
  props: ["infoCard", "routePath"],
  methods: {
    getAnimalImgPath(engname) {
      let images = require(`@/assets/images/image_animal/${engname}.png`);
      return images;
    },
    getFishImgPath(name) {
      let images = require(`@/assets/images/image_fishes/${name}.png`);
      return images;
    },
    getInsectImgPath(name) {
      let images = require(`@/assets/images/image_insect/${name}.png`);
      return images;
    },
    getFossilImgPath() {
      let images = require(`@/assets/images/fossil.png`);
      return images;
    }
  }
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
