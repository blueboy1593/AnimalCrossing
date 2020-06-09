<template>
  <div>
    <div style="display: flex;">
      <v-text-field
        v-model="searchText"
        @keyup="filter"
        solo-inverted
        flat
        hide-details
        label="Search"
        class="nav-search"
      ></v-text-field>
    </div>
    <div class="neighborCards">
      <tradeCard
        v-for="tradeCard in searchItemCards"
        :key="tradeCard.id"
        :infoCard="tradeCard"
        :routePath="routePath"
        :category="category"
      />
    </div>
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
      category: "animal",
      routePath: this.$route.path,
      tradeCards: [],
      searchItemCards: [],
      searchText: ""
    };
  },
  methods: {
    filter() {
      let check = this.tradeCards.filter(
        tradeCard => tradeCard.name.indexOf(this.searchText.trim()) !== -1
      );
      this.searchItemCards = check;
    }
  },

  async mounted() {
    this.tradeCards = await getNeighbors();
    this.searchItemCards = this.tradeCards;
  }
};
</script>

<style scoped>
.v-text-field {
  width: 300px;
  background-color: rgba(173, 204, 245, 0.322);
  margin-bottom: 10px;
  margin-left: 35%;
  margin-right: 35%;
}
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
