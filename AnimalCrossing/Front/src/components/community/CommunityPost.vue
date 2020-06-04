<template>
  <div>
    <div>
      <communityCard
        v-for="communityCard in communityCards"
        :key="communityCard.id"
        :communityCard="communityCard"
        class="card_one"
      />
    </div>
    <router-link to="/community/write">
      <button class="write_btn btn btn-primary">
        글쓰기
      </button>
    </router-link>
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

<style scoped>
.card_one {
  display: inline-block;
}

.write_btn {
  border: 0;
  background: none;
  display: inline-block;
  margin: 10px auto 0px;
  text-align: center;
  padding: 0px 40px;
  height: 40px;
  outline: none;
  color: white;
  border-radius: 24px;
  transition: 0.25s;
  cursor: pointer;
  border: 2px solid #e46fc7;
}

.write_btn:hover {
  background: #e46fc7;
}
</style>
