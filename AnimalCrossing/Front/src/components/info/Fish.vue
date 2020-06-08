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
    
    <!-- <div class="dogam">물고기 도감</div> -->
    <div class="fishCards">
      <infoCard
        v-for="infoCard in selectedCards"
        :key="infoCard.title"
        :infoCard="infoCard"
        :routePath="routePath"
      />
    </div>
  </div>
</template>

<script>
import { getFishes } from "@/api/info.js";
import infoCard from "./infoCard.vue";

export default {
  name: "fish",
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
      searchText: "",
      selectedCards: []
    };
  },
  async mounted() {
    this.infoCards = await getFishes(this.infoCards);
    this.selectedCards = this.infoCards;
  }
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Jua&display=swap");

 .v-text-field{
   width: 300px;
   background-color: rgba(173, 204, 245, 0.322);
   margin-bottom: 10px;
   margin-left: 35%;
   margin-right: 35%;
 }

.dogam {
  text-align: center;
  font-family: "Jua", sans-serif;
  color: rgb(9, 40, 71);
}

.fishCards {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  grid-auto-rows: auto;
  grid-gap: 1rem 1rem;
}

@media (max-width: 1600px) {
  .fishCards {
    grid-template-columns: repeat(6, 1fr);
    grid-gap: 1rem 0.4rem;
  }
}

@media (max-width: 1300px) {
  .fishCards {
    grid-template-columns: repeat(5, 1fr);
    grid-gap: 1rem 0.4rem;
  }
}

@media (max-width: 1100px) {
  .fishCards {
    grid-template-columns: repeat(4, 1fr);
    grid-gap: 1rem 0.4rem;
  }
}

@media (max-width: 900px) {
  .fishCards {
    grid-template-columns: repeat(3, 1fr);
    grid-gap: 1rem 0rem;
  }
}

@media (max-width: 560px) {
  .fishCards {
    grid-template-columns: repeat(2, 1fr);
    grid-gap: 1rem 0rem;
  }
}
</style>
