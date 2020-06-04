<template>
  <div class="commentitem">
    <p>{{ comment.content }}</p>
  </div>
</template>

<script>
import * as showService from "../../api/show.js";
export default {
  name: "commentListItem",
  props: {
    comment: {
      type: Object,
      required: false
    }
  },
  data() {
    return {
      comments: []
    };
  },
  mounted: async function() {
    var showId = this.$route.params.id;
    const data = await showService.getShowById(showId);
    console.log(data);
  }
};
</script>

<style></style>
