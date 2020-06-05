!<template>
  <div class="neighborCards">
    <!-- <h1>여기는 동물주민거래 게시판이지롱</h1> -->
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
import { getNeighbors } from "@/api/info.js";
import tradeCard from "../trade/tradeCard.vue";
export default {
  name: "tradeNeighbors",
  components: {
    tradeCard
  },
  data() {
    return {
      tradeCards: [],
      detailTrade: [],
      routePath: this.$route.path,
      category: "neighbor"
    };
  },
  async mounted() {
    this.tradeCards = await getNeighbors(this.tradeCards);
  },
  methods: {
    routePushTo(neighbor_id) {
      console.log(neighbor_id);
      this.$router.push(`/trade/detail/${neighbor_id}`);
    }
  }
};
</script>

<style scoped>
.neighborCards {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  grid-auto-rows: auto;
  grid-gap: 1rem 1rem;
  /* grid-template-columns: repeat(auto-fill, minmax(100px, 1fr)); */
}
@media (max-width: 1600px) {
  .neighborCards {
    grid-template-columns: repeat(6, 1fr);
    grid-gap: 1rem 0.4rem;
  }
}

@media (max-width: 1300px) {
  .neighborCards {
    grid-template-columns: repeat(5, 1fr);
    grid-gap: 1rem 0.4rem;
  }
}

@media (max-width: 1100px) {
  .neighborCards {
    grid-template-columns: repeat(4, 1fr);
    grid-gap: 1rem 0.4rem;
  }
}

@media (max-width: 900px) {
  .neighborCards {
    grid-template-columns: repeat(3, 1fr);
    grid-gap: 1rem 0rem;
  }
}

@media (max-width: 560px) {
  .neighborCards {
    grid-template-columns: repeat(2, 1fr);
    grid-gap: 1rem 0rem;
  }
}
</style>
