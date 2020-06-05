<template>
  <div class="infoCard">
    <div class="photo">
      <img
        v-if="
          (routePath === '/info/neighbor') | (routePath === '/trade/neighbor')
        "
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
        v-if="(routePath === '/info/fossil') | (routePath === '/trade/fossil')"
        :src="getFossilImgPath()"
        class="image"
      />
      <img
        v-if="
          (routePath === '/info/painting') | (routePath === '/trade/painting')
        "
        :src="getPatingImagPath(infoCard.engname)"
        class="image"
        @click="paintingDialog = !paintingDialog"
      />
    </div>
    <div class="infoName">
      {{ infoCard.name }}
    </div>
    <div v-if="routePath === '/info/insect'">
      <div class="infoDetail">
        {{ infoCard.month }}
      </div>
      <div class="infoDetail">
        {{ infoCard.time }}
      </div>
    </div>
    <div v-if="routePath === '/info/fish'">
      <div class="infoDetail">
        {{ infoCard.month }}
      </div>
      <div class="infoDetail">
        {{ infoCard.time }}
      </div>
    </div>
    <div v-if="routePath === '/info/fossil'">
      <div class="infoDetail">
        {{ infoCard.price + " 벨" }}
      </div>
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

    <v-dialog
      v-if="routePath === '/info/painting'"
      id="paintingDialog"
      v-model="paintingDialog"
      width="600"
    >
      <PaintingDialog
        id="paintingDialog"
        v-model="paintingDialog"
        v-on:close="paintingDialog = false"
        :infoCard="infoCard"
      />
    </v-dialog>
  </div>
</template>

<script>
import PaintingDialog from "@/components/info/infoDetail.vue";

export default {
  name: "infoCard",
  components: {
    PaintingDialog
  },
  props: ["infoCard", "routePath"],
  data: () => ({
    paintingDialog: false
  }),
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
    }
  }
};
</script>

<style>
.infoCard {
  margin-top: 0.3rem;
  width: 120px;
  /* height: 172px; */
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
