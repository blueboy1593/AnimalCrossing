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
  background-color: rgba(30, 143, 255, 0.075);
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
  border-bottom: 1.2px solid rgba(76, 180, 157, 0.295);
  margin-bottom: 0.3rem;
  height: 50px;
  line-height: 50px;
  display: grid;
  grid-template-columns: 1fr 3fr 1fr;
  grid-template-areas: 
    "user comment time";
}

.onecomment:hover {
  opacity: 0.8;
  font-weight: bold;
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
