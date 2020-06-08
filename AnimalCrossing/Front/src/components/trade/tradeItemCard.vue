<template>
  <div>
    <router-link
      :to="{
        name: 'tradedetail',
        params: { id: tradeItemCard.id, image_url: image_url }
      }"
    >
      <div class="cCard">
        <div class="cphoto">
          <!-- <div v-if="tradeItemCard.image === null"> -->
          <img :src="getImgPath()" class="cimage" />
          <!-- </div> -->
          <!-- <div v-else>
            <img v-bind:src="tradeItemCard.image" alt="" class="detailimage" />
          </div> -->
        </div>
        <div class="infoName">
          {{ tradeItemCard.title }}
        </div>
        <v-row>
          <v-col>
            <div class="infoDetail3">
              {{ tradeItemCard.username }}
            </div></v-col
          ><v-col>
            <div class="infoDetail4">
              {{ tradeItemCard.price }}
            </div></v-col
          ><v-col>
            <div class="infoDetail2">
              {{ tradeItemCard.created_at.substring(0, 10) }}
            </div></v-col
          ></v-row
        >
      </div>
    </router-link>
  </div>
</template>

<script>
// import * as infoService from "../../api/info.js";
export default {
  name: "tradeItemCard",
  props: ["tradeItemCard", "engname", "category"],
  data() {
    return {
      image_url: ""
    };
  },
  methods: {
    getImgPath() {
      let image = "";
      if (this.category === "fossil") {
        image = require(`@/assets/images/fossil.png`);
      } else if (this.category === "painting") {
        image = require(`@/assets/images/image_${this.category}/${this.engname}.jpg`);
      } else if (this.category === "animal") {
        image = require(`@/assets/images/image_${this.category}/${this.engname}.png`);
      }
      this.image_url = image;
      return image;
    }
  }
};
</script>

<style scoped>
.cCard {
  display: inline-block;
  margin-top: 0.3rem;
  width: 26rem;
  height: 20%;
  border-radius: 15px;
  margin-right: 1rem;
  overflow: hidden;
  margin-left: 0.5rem;
  color: black;
  background-color: rgba(110, 173, 157, 0.144);
}

.cCard:hover {
  background-color: rgba(98, 173, 155, 0.26);
  transform: scale(1.03);
  opacity: 0.9;
  box-shadow: 0 0 0 1px #76a7b2;
}

.cphoto {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  min-height: 246.4px;
  height: 20%;
  border-radius: 15px;
  text-align: center;
  overflow: hidden;
}

.cimage {
  max-height: 170px;
  display: block;
  margin: 0 auto;
  margin-top: 4%;
}

.detailimage {
  width: auto;
  height: auto;
  max-width: 460px;
  max-height: 240px;
}

.infoName {
  text-align: center;
  font-weight: bolder;
  font-size: 1rem;
  font-family: "Gamja Flower", cursive;
}

.infoDetail3 {
  font-weight: 100;
  font-family: "Gamja Flower", cursive;
  margin-left: 10px;
}
.infoDetail4 {
  font-weight: 100;
  font-family: "Gamja Flower", cursive;
  margin-left: 20px;
  text-align: center;
}

.infoDetail2 {
  text-align: right !important;
  font-weight: 100;
  font-family: "Gamja Flower", cursive;
  margin-right: 10px;
}
</style>
