<template>
  <div class="onecomment">
    <div class="user">
      {{ CommentList.username }}
    </div>
    <p class="comment">
      {{ CommentList.content }}
    </p>
    <p class="time">
      {{ CommentList.created_at }}
    </p>
    <v-btn color="error" small class="delete" @click="deleteComment"
      >삭제</v-btn
    >
  </div>
</template>

<script>
import * as tradeService from "../../api/trade.js";
export default {
  name: "CommentList",
  props: ["CommentList"],
  methods: {
    async deleteComment() {
      var scope = this;
      const token = this.$store.state.user.token;
      const comment_pk = this.CommentList.id;
      await tradeService.deleteCommentApi(comment_pk, token, function(
        response
      ) {
        console.log(response);
        scope.$emit("update");
      });
    }
  }
};
</script>

<style scoped>
.onecomment {
  background-color: rgba(30, 143, 255, 0.075);
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
  border-bottom: 1.2px solid rgba(76, 180, 157, 0.295);
  margin-bottom: 0.3rem;
  height: 50px;
  /* line-height: 50px; */
  display: grid;
  grid-template-columns: 1fr 3fr 1fr 0.2fr;
  grid-template-areas: "user comment time delete";
}

.onecomment:hover {
  opacity: 0.8;
  font-weight: bold;
}

.user {
  display: grid;
  grid-area: user;
  text-align: center;
  font-family: "Gamja Flower";
  font-size: 1.2rem;
}

.comment {
  display: grid;
  grid-area: comment;
  font-family: "Gamja Flower";
  font-size: 1.2rem;
}

.time {
  display: grid;
  grid-area: time;
  text-align: center;
  font-family: "Gamja Flower";
  font-size: 1.2rem;
}

.delete {
  width: 2%;
  height: 1%;
  z-index: 1;
  margin-top: 10px;
  margin-right: 5px;
  opacity: 55%;
  color: white;
  font-family: "Gamja Flower";
  font-size: 1rem;
}
</style>
