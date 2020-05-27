<template>
  <div class="fossilCards">
    <!-- <h1>fish</h1> -->
    <infoCard
      v-for="infoCard in infoCards"
      :key="infoCard.title"
      :infoCard="infoCard"
    />
  </div>
</template>

<script>
import infoCard from "./infoCard.vue";

export default {
  name: "fossil",
  components: {
      infoCard
  },
  data () {
    return {
      infoCards: [
        {
          src: require('../../assets/images/fossil.png'),
          title: '화석',
        },
        {
          src: require('../../assets/images/fossil.png'),
          title: '화석',
        },
        {
          src: require('../../assets/images/fossil.png'),
          title: '화석',
        },
        {
          src: require('../../assets/images/fossil.png'),
          title: '화석',
        },
        {
          src: require('../../assets/images/fossil.png'),
          title: '화석',
        },
        {
          src: require('../../assets/images/fossil.png'),
          title: '화석',
        },
        {
          src: require('../../assets/images/fossil.png'),
          title: '화석',
        },
        {
          src: require('../../assets/images/fossil.png'),
          title: '화석',
        },
      ]
    }
  }
};
</script>

<style>
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