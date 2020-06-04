<template>
  <div>
    <ul>
      <div v-for="comment in comments" :key="comment.id">
        <li>
          <CommentListItem :comment="comment" />
        </li>
      </div>
    </ul>
  </div>
</template>

<script>
import CommentListItem from "./CommunityComment.vue";
export default {
  name: "commentList",
  components: {
    CommentListItem
  },
  props: {
    comments: {
      type: Array,
      required: false
    }
  }
};
</script>

<style></style>
