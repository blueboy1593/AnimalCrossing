<template>
  <div class="onecomment">
    <p>{{ CommentList.username }}</p>
    <p>{{ CommentList.content }}</p>
    <p>{{ CommentList.created_at }}</p>
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
  border: 2px solid blue;
  border-radius: 10px;
}
</style>
