<template>
  <div class="fishCards">
    <!-- <h1>fish</h1> -->
    <infoCard
      v-for="infoCard in infoCards"
      :key="infoCard.title"
      :infoCard="infoCard"
    />
  </div>
</template>

<script>
import axios from "axios";
import infoCard from "./infoCard.vue";

export default {
  name: "fish",
  components: {
    infoCard
  },
  methods: {
    getFish: function() {
      axios
        .get("http://127.0.0.1:8000/api/v1/fishes/")
        .then(function(response) {
          console.log(response.data);
          // 여기서 가져온 데이터 for문으로 로드하기
        })
        .catch(function(error) {
          console.log(error);
        });
    }
  },
  mounted() {
    this.getFish();
  },
  data() {
    return {
      infoCards: [
        {
          src: require("../../assets/images/fish.png"),
          title: "붕어",
          detail: "5월"
        },
        {
          src: require("../../assets/images/fish.png"),
          title: "잉어",
          detail: "5월"
        },
        {
          src: require("../../assets/images/fish.png"),
          title: "흰동가리",
          detail: "5월"
        },
        {
          src: require("../../assets/images/fish.png"),
          title: "흰동가리",
          detail: "5월"
        },
        {
          src: require("../../assets/images/fish.png"),
          title: "흰동가리",
          detail: "5월"
        },
        {
          src: require("../../assets/images/fish.png"),
          title: "흰동가리",
          detail: "5월"
        },
        {
          src: require("../../assets/images/fish.png"),
          title: "흰동가리",
          detail: "5월"
        },
        {
          src: require("../../assets/images/fish.png"),
          title: "흰동가리",
          detail: "5월"
        },
        {
          src: require("../../assets/images/fish.png"),
          title: "흰동가리",
          detail: "5월"
        },
        {
          src: require("../../assets/images/fish.png"),
          title: "흰동가리",
          detail: "5월"
        },
        {
          src: require("../../assets/images/fish.png"),
          title: "흰동가리",
          detail: "5월"
        },
        {
          src: require("../../assets/images/fish.png"),
          title: "흰동가리",
          detail: "5월"
        },
        {
          src: require("../../assets/images/fish.png"),
          title: "흰동가리",
          detail: "5월"
        }
      ]
    };
  }
};
</script>

<style>
.fishCards {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  grid-auto-rows: auto;
  grid-gap: 1rem 1rem;
  /* grid-template-columns: repeat(auto-fill, minmax(100px, 1fr)); */
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
