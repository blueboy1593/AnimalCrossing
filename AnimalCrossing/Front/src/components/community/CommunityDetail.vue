<template>
  <div class="community">
    <div class="container">
      <h2 class="ttext" style="margin-bottom: 5px">{{ this.article.title }}</h2>
      <v-row no-gutters>
        <v-col>
          <p>{{ this.article.username }}</p>
        </v-col>
        <v-col>
          <p style="text-align:right">{{ this.article.created_at }}</p>
        </v-col>
      </v-row>
      <div v-if="this.image == ''">
        <img
          src="https://ichef.bbci.co.uk/news/976/cpsprodpb/CA15/production/_111633715_df2cb9e9-4f34-499d-a255-29abf37d36d0.jpg"
          class="cimage"
        />
      </div>
      <div v-else><img v-bind:src="image" alt="" class="detailimage" /></div>
      <div class="showcontent">
        <p>{{ article.content }}</p>
      </div>
      <h2>comment 넣을 곳</h2>
      <CommentList />
    </div>
  </div>
</template>

<script>
import * as showService from "../../api/show.js";
import CommentList from "./CommunityCommentList.vue";

export default {
  components: { CommentList },
  data: function() {
    return {
      article: {
        title: "",
        content: "",
        image: "",
        username: "",
        created_at: ""
      }
    };
  },
  mounted: async function() {
    var showId = this.$route.params.id;
    const data = await showService.getShowById(showId);
    this.article.title = data.title;
    this.article.image = data.image;
    this.article.content = data.content;
    this.article.created_at = data.created_at;
    this.article.username = data.username;
  }
};
</script>

<style>
.detailimage {
  width: 60%;
  align-items: center;
  display: block;
  margin: 0px auto;
}
.ttext {
  text-align: center;
}
.showcontent {
  margin-top: 10px;
}
</style>
