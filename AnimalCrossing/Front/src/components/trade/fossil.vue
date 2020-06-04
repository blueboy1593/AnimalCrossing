!<template>
  <div>
    <h1>여기는 화석거래 게시판이지롱</h1>
    <!-- <tradeCard
      v-for="tradeCard in tradeCards"
      :key="tradeCard.id"
      :tradeCard="tradeCard"
    /> -->
  </div>
</template>

<script>
import { getFossils } from "@/api/info.js";
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
    this.tradeCards = await getFossils(this.tradeCards);
  }
};
</script>

<style></style>
