<template>
  <div>
    <ul>
      <div v-for="comment in comments" :key="comment.id">
        <li>
          <p>{ comment.content }</p>
        </li>
      </div>
    </ul>
  </div>
</template>

<script>
export default {
  name: "commentList",
  props: {
    comments: {
      type: Array,
      required: false
    }
  }
};
</script>

<style></style>
