<template>
  <div>
    <communityCard
      xs12
      sm12
      md6
      lg6
      xl6
      v-for="communityCard in communityCards"
      :key="communityCard.id"
      :communityCard="communityCard"
    />
  </div>
</template>

<script>
import { getShows } from "@/api/show.js";
import communityCard from "./CommunityCard.vue";

export default {
  name: "community",
  components: {
    communityCard
  },
  data() {
    return {
      communityCards: []
    };
  },
  async mounted() {
    this.communityCards = await getShows(this.communityCards);
  }
};
</script>

<style></style>
