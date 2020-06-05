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
  </div>
</template>

<script>
export default {
  name: "CommentList",
  props: ["CommentList"]
};
</script>

<style>
.onecomment {
  /* border: 1px solid blue; */
  background-color: rgba(30, 143, 255, 0.075);
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
  /* border-radius: 10px; */
  /* border-bottom: 1.2px solid rgba(30, 143, 255, 0.295); */
  border-bottom: 1.2px solid rgba(76, 180, 157, 0.295);
  margin-bottom: 0.3rem;
  height: 50px;
  line-height: 50px;
  /* font-weight: bold; */
  display: grid;
  grid-template-columns: 1fr 3fr 1fr;
  grid-template-areas: 
    "user comment time";
}

.user {
  display: grid;
  grid-area: user;
  text-align: center;
}

.comment {
  display: grid;
  grid-area: comment;
}

.time {
  display: grid;
  grid-area: time;
  text-align: center;
}
</style>
