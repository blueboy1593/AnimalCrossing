<template>
  <div>
    <router-link :to="{ name: 'etcdetail', params: { id: TradeEtcCard.id } }">
      <div class="cCard">
        <div class="cphoto">
          <div v-if="TradeEtcCard.image === null">
            <img
              src="https://ichef.bbci.co.uk/news/976/cpsprodpb/CA15/production/_111633715_df2cb9e9-4f34-499d-a255-29abf37d36d0.jpg"
              class="cimage"
            />
          </div>
          <div v-else>
            <img v-bind:src="TradeEtcCard.image" alt="" class="detailimage" />
          </div>
        </div>
        <div class="infoName">
          {{ TradeEtcCard.title }}
        </div>
        <v-row>
          <v-col>
            <div class="infoDetail3">
              {{ TradeEtcCard.username }}
            </div></v-col
          ><v-col>
            <div class="infoDetail4">
              {{ TradeEtcCard.price }}
            </div></v-col
          ><v-col>
            <div class="infoDetail2">
              {{ TradeEtcCard.created_at.substring(0, 10) }}
            </div></v-col
          ></v-row
        >
      </div>
    </router-link>
  </div>
</template>

<script>
export default {
  name: "TradeEtcCard",
  props: ["TradeEtcCard"]
};
</script>

<style scoped>
.cCard {
  color: black;
  display: inline-block;
  margin-top: 0.3rem;
  width: 26rem;
  height: 20%;
  border-radius: 15px;
  margin-right: 1rem;
  color: black;
  overflow: hidden;

  background-color: rgba(110, 173, 157, 0.144);
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
