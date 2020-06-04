<template>
  <div class="community">
    <h3 style="font-family:Gamja Flower">자랑해요, 동물의 숲</h3>
    <v-btn>글쓰기</v-btn>
    <CommunityPost />
  </div>
</template>

<script>
import CommunityPost from "../components/community/CommunityPost.vue";
export default {
  components: {
    CommunityPost
  }
};
</script>

<style></style>
