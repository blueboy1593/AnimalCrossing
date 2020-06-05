!<template>
  <div class="fossilCards">
    <h1>여기는 화석거래 게시판이지롱</h1>
    <tradeCard
      v-for="tradeCard in tradeCards"
      :key="tradeCard.id"
      :infoCard="tradeCard"
      :routePath="routePath"
    />
  </div>
</template>

<script>
import { getFossils } from "@/api/info.js";
import tradeCard from "../info/infoCard.vue";
export default {
  name: "tradeNeighbors",
  components: {
    tradeCard
  },
  data() {
    return {
      tradeCards: [],
      routePath: this.$route.path
    };
  },
  async mounted() {
    this.tradeCards = await getFossils(this.tradeCards);
  }
};
</script>

<style scoped>
.fossilCards {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  grid-auto-rows: auto;
  grid-gap: 1rem 1rem;
  /* grid-template-columns: repeat(auto-fill, minmax(100px, 1fr)); */
}
@media (max-width: 1600px) {
  .fossilCards {
    grid-template-columns: repeat(6, 1fr);
    grid-gap: 1rem 0.4rem;
  }
}

@media (max-width: 1300px) {
  .fossilCards {
    grid-template-columns: repeat(5, 1fr);
    grid-gap: 1rem 0.4rem;
  }
}

@media (max-width: 1100px) {
  .fossilCards {
    grid-template-columns: repeat(4, 1fr);
    grid-gap: 1rem 0.4rem;
  }
}

@media (max-width: 900px) {
  .fossilCards {
    grid-template-columns: repeat(3, 1fr);
    grid-gap: 1rem 0rem;
  }
}

@media (max-width: 560px) {
  .fossilCards {
    grid-template-columns: repeat(2, 1fr);
    grid-gap: 1rem 0rem;
  }
}
</style>
