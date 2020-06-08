<template>
  <div>
    <router-link
      :to="{ name: 'tradedetail', params: { id: tradeItemCard.id } }"
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
        <div class="cphoto"></div>
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
    return {};
  },
  methods: {
    getImgPath() {
      let image = require(`@/assets/images/image_${this.category}/${this.engname}.png`);
      console.log(`@/assets/images/image_${this.category}/${this.engname}.png`);
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
  background-color: rgba(110, 173, 157, 0.144);
  color: black;
}

.cCard:hover {
  border-bottom: 1px solid #76a7b2;
  background-color: rgba(98, 173, 155, 0.26);
}

.cphoto {
  width: 100%;
  height: 20%;
  border-radius: 15px;
  text-align: center;
  overflow: hidden;
}

.cimage {
  height: 170px;
  display: block;
  margin: 0 auto;
}

.detailimage {
  width: 100%;
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
