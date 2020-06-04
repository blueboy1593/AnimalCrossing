!<template>
  <div>
    <h1>여기는 미술품 거래 게시판이지롱</h1>
    <!-- <tradeCard
      v-for="tradeCard in tradeCards"
      :key="tradeCard.id"
      :tradeCard="tradeCard"
    /> -->
  </div>
</template>

<script>
import { getPaintings } from "@/api/info.js";
// import tradeCard from "../info/infoCard.vue";
export default {
  name: "tradeNeighbors",
  components: {
    // tradeCard
  },
  data() {
    return {
      tradeCards: []
    };
  },
  async mounted() {
    this.tradeCards = await getPaintings(this.tradeCards);
  }
};
</script>

<style></style>
