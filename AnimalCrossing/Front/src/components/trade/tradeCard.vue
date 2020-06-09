<template>
  <div class="infoCard" @click="routePushTo(category, infoCard.id)">
    <div class="photo">
      <!-- 동물주민 이미지 가져오기 -->
      <img
        v-if="routePath === '/trade/neighbor'"
        :src="getAnimalImgPath(infoCard.engname)"
        class="image"
      />

      <!-- 화석 이미지 가져오기 -->
      <img
        v-if="routePath === '/trade/fossil'"
        :src="getFossilImgPath()"
        class="image"
      />

      <!-- 미술품 이미지 가져오기 -->
      <img
        v-if="routePath === '/trade/painting'"
        :src="getPatingImagPath(infoCard.engname)"
        class="image"
      />
    </div>
    <div class="infoName">
      {{ infoCard.name }}
    </div>
    <div v-if="routePath === '/info/fossil'">
      <div class="infoDetail">
        {{ infoCard.price + " 벨" }}
      </div>
      <div v-if="routePath === '/info/neighbor'">
        <div class="infoDetail">
          {{ infoCard.personality }}
        </div>
        <div class="infoDetail">
          {{ infoCard.sort }}
        </div>
      </div>
      <div v-if="routePath === '/info/painting'">
        <div class="infoDetail">
          {{ infoCard.real }}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "infoCard",
  props: ["infoCard", "routePath", "category"],
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
    },
    getPatingImagPath(engname) {
      let images = require(`@/assets/images/image_painting/${engname}.jpg`);
      return images;
    },
    routePushTo(category, id) {
      this.$router.push(`/trade/list/${category}/${id}`);
    }
  }
};
</script>

<style scoped>
.infoCard {
  margin-left: 5px;
  margin-top: 0.3rem;
  width: 120px;
  /* height: 172px; */
  border-radius: 15px;
  background-color: #c1d2e1;
  overflow: hidden;
  color: black;
}

.infoCard:hover {
  transform: scale(1.03);
  opacity: 0.9;
  box-shadow: 0 0 0 3px #276dd68e;
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
  font-size: 1rem;
  font-family: "Gamja Flower";
}

.infoDetail {
  text-align: center;
  font-weight: 100;
  font-family: "Gamja Flower";
  font-size: 1rem;
}
</style>
