<template>
  <div class="paintingCards">
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
  name: "painting",
  components: {
      infoCard
  },
  data () {
    return {
      infoCards: [
        {
          src: require('../../assets/images/art.jpg'),
          title: '미술품',
        },
        {
          src: require('../../assets/images/art.jpg'),
          title: '미술품',
        },
        {
          src: require('../../assets/images/art.jpg'),
          title: '미술품',
        },
        {
          src: require('../../assets/images/art.jpg'),
          title: '미술품',
        },
        {
          src: require('../../assets/images/art.jpg'),
          title: '미술품',
        },
        {
          src: require('../../assets/images/art.jpg'),
          title: '미술품',
        },
        {
          src: require('../../assets/images/art.jpg'),
          title: '미술품',
        },
        {
          src: require('../../assets/images/art.jpg'),
          title: '미술품',
        },
        {
          src: require('../../assets/images/art.jpg'),
          title: '미술품',
        },
      ]
    }
  }
};
</script>

<style>
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