<template>
  <div class="insectCards">
    <infoCard
      v-for="infoCard in infoCards"
      :key="infoCard.id"
      :infoCard="infoCard"
      :routePath="routePath"
    />
  </div>
</template>

<script>
import axios from "axios";
import infoCard from "./infoCard.vue";

export default {
  name: "insect",
  components: {
    infoCard
  },
  data() {
    return {
      infoCards: [],
      routePath: this.$route.path
    };
  },
  methods: {
    getInsect: function() {
      axios
        .get("http://127.0.0.1:8000/api/v1/insects/")
        .then(response => {
          this.infoCards = response.data;
          console.log("this.infoCards::: ", this.infoCards);
        })
        .catch(error => {
          console.log(error);
        });
    }
  },
  mounted() {
    this.getInsect();
  }
  // data() {
  //   return {
  //     infoCards: [
  //       {
  //         src: require("../../assets/images/bug.png"),
  //         title: "나비"
  //       },
  //       {
  //         src: require("../../assets/images/bug.png"),
  //         title: "나비"
  //       },
  //       {
  //         src: require("../../assets/images/bug.png"),
  //         title: "나비"
  //       },
  //       {
  //         src: require("../../assets/images/bug.png"),
  //         title: "나비"
  //       },
  //       {
  //         src: require("../../assets/images/bug.png"),
  //         title: "나비"
  //       },
  //       {
  //         src: require("../../assets/images/bug.png"),
  //         title: "나비"
  //       },
  //       {
  //         src: require("../../assets/images/bug.png"),
  //         title: "나비"
  //       },
  //       {
  //         src: require("../../assets/images/bug.png"),
  //         title: "나비"
  //       },
  //       {
  //         src: require("../../assets/images/bug.png"),
  //         title: "나비"
  //       },
  //       {
  //         src: require("../../assets/images/bug.png"),
  //         title: "나비"
  //       }
  //     ]
  //   };
  // }
};
</script>

<style>
.insectCards {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  grid-auto-rows: auto;
  grid-gap: 1rem 1rem;
  /* grid-template-columns: repeat(auto-fill, minmax(100px, 1fr)); */
}
@media (max-width: 1600px) {
  .insectCards {
    grid-template-columns: repeat(6, 1fr);
    grid-gap: 1rem 0.4rem;
  }
}

@media (max-width: 1300px) {
  .insectCards {
    grid-template-columns: repeat(5, 1fr);
    grid-gap: 1rem 0.4rem;
  }
}

@media (max-width: 1100px) {
  .insectCards {
    grid-template-columns: repeat(4, 1fr);
    grid-gap: 1rem 0.4rem;
  }
}

@media (max-width: 900px) {
  .insectCards {
    grid-template-columns: repeat(3, 1fr);
    grid-gap: 1rem 0rem;
  }
}

@media (max-width: 560px) {
  .insectCards {
    grid-template-columns: repeat(2, 1fr);
    grid-gap: 1rem 0rem;
  }
}
</style>
