<template>
  <div class="neighborCards">
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
  name: "neighbor",
  components: {
      infoCard
  },
  data () {
    return {
      infoCards: [
        {
          src: require('../../assets/images/neighbor.png'),
          title: '이웃',
        },
        {
          src: require('../../assets/images/neighbor.png'),
          title: '이웃',
        },
        {
          src: require('../../assets/images/neighbor.png'),
          title: '이웃',
        },
        {
          src: require('../../assets/images/neighbor.png'),
          title: '이웃',
        },
        {
          src: require('../../assets/images/neighbor.png'),
          title: '이웃',
        },
        {
          src: require('../../assets/images/neighbor.png'),
          title: '이웃',
        },
        {
          src: require('../../assets/images/neighbor.png'),
          title: '이웃',
        },
        {
          src: require('../../assets/images/neighbor.png'),
          title: '이웃',
        },
        {
          src: require('../../assets/images/neighbor.png'),
          title: '이웃',
        },
      ]
    }
  }
};
</script>

<style>
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