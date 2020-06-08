<template>
  <div>
    <v-text-field
      v-model="searchText"
      @keyup="filter"
      solo-inverted
      flat
      hide-details
      label="Search"
      class="nav-search"
    ></v-text-field>
    <div class="neighborCards">
      <infoCard
        v-for="infoCard in selectedCards"
        :key="infoCard.id"
        :infoCard="infoCard"
        :routePath="routePath"
      />
    </div>
  </div>
</template>

<script>
import { getNeighbors } from "@/api/info.js";
import infoCard from "./infoCard.vue";

export default {
  name: "neighbor",
  components: {
    infoCard
  },
  methods: {
    filter() {
      let check = this.infoCards.filter(
        infoCard => infoCard.name.indexOf(this.searchText.trim()) !== -1
      );
      this.selectedCards = check;
    }
  },
  data() {
    return {
      infoCards: [],
      routePath: this.$route.path,
      selectedCards: [],
      searchText: ""
    };
  },
  async mounted() {
    this.infoCards = await getNeighbors(this.infoCards);
    console.log(this.infoCards);
    this.selectedCards = this.infoCards;
  }
  // data() {
  //   return {
  //     infoCards: [
  //       {
  //         src: require("../../assets/images/neighbor.png"),
  //         title: "이웃"
  //       },
  //       {
  //         src: require("../../assets/images/neighbor.png"),
  //         title: "이웃"
  //       },
  //       {
  //         src: require("../../assets/images/neighbor.png"),
  //         title: "이웃"
  //       },
  //       {
  //         src: require("../../assets/images/neighbor.png"),
  //         title: "이웃"
  //       },
  //       {
  //         src: require("../../assets/images/neighbor.png"),
  //         title: "이웃"
  //       },
  //       {
  //         src: require("../../assets/images/neighbor.png"),
  //         title: "이웃"
  //       },
  //       {
  //         src: require("../../assets/images/neighbor.png"),
  //         title: "이웃"
  //       },
  //       {
  //         src: require("../../assets/images/neighbor.png"),
  //         title: "이웃"
  //       },
  //       {
  //         src: require("../../assets/images/neighbor.png"),
  //         title: "이웃"
  //       }
  //     ]
  //   };
  // }
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
