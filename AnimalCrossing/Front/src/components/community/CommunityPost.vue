<template>
  <div>
    <h2 class="btitle">자랑해요, 동물의 숲</h2>
    <div class="writeDiv">
      <div v-if="!$store.state.isSigned">
        <router-link to="/login">
          <img
            src="../../assets/images/write.png"
            alt="글쓰기"
            class="nav-img"
          />
        </router-link>
      </div>
      <div v-else>
        <router-link to="/community/write">
          <img
            src="../../assets/images/write.png"
            alt="글쓰기"
            class="nav-img"
          />
        </router-link>
      </div>
    </div>
    <div>
      <communityCard
        v-for="communityCard in communityCards"
        :key="communityCard.id"
        :communityCard="communityCard"
        class="card_one"
      />
    </div>
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
  color: black;
  border-radius: 24px;
  transition: 0.25s;
  cursor: pointer;
  border: 2px solid #e46fc7;
}

.write_btn:hover {
  background: #e46fc7;
}

.writeDiv {
  display: flex;
  justify-content: flex-end;
  margin-right: 3%;
}

.nav-img {
  height: 60px;
  margin-right: 30px;
}

.btitle {
  font-family: "Jua", sans-serif;
  text-align: center;
  font-size: 1.7rem;
}
</style>
