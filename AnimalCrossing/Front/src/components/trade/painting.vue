<template>
  <div class="paintingCards">
    <tradeCard
      v-for="tradeCard in tradeCards"
      :key="tradeCard.id"
      :infoCard="tradeCard"
      :routePath="routePath"
      :category="category"
    />
  </div>
</template>

<script>
import { getPaintings } from "@/api/info.js";
import tradeCard from "../trade/tradeCard.vue";
export default {
  name: "tradeNeighbors",
  components: {
    tradeCard
  },
  data() {
    return {
      tradeCards: [],
      routePath: this.$route.path,
      category: "painting"
    };
  },
  async mounted() {
    this.tradeCards = await getPaintings(this.tradeCards);
    console.log("hi", this.tradeCards);
  }
};
</script>

<style scoped>
.paintingCards {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  grid-auto-rows: auto;
  grid-gap: 1rem 1rem;
  /* grid-template-columns: repeat(auto-fill, minmax(100px, 1fr)); */
}
@media (max-width: 1600px) {
  .paintingCards {
    grid-template-columns: repeat(6, 1fr);
    grid-gap: 1rem 0.4rem;
  }
}

@media (max-width: 1300px) {
  .paintingCards {
    grid-template-columns: repeat(5, 1fr);
    grid-gap: 1rem 0.4rem;
  }
}

@media (max-width: 1100px) {
  .paintingCards {
    grid-template-columns: repeat(4, 1fr);
    grid-gap: 1rem 0.4rem;
  }
}

@media (max-width: 900px) {
  .paintingCards {
    grid-template-columns: repeat(3, 1fr);
    grid-gap: 1rem 0rem;
  }
}

@media (max-width: 560px) {
  .paintingCards {
    grid-template-columns: repeat(2, 1fr);
    grid-gap: 1rem 0rem;
  }
}
</style>
