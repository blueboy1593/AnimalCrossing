<template>
  <div class="community">
    <div class="container">
      <h2 class="ttext" style="margin-bottom: 5px">{{ article.title }}</h2>
      <v-row no-gutters>
        <v-col>
          <p>{{ article.username }}</p>
        </v-col>
        <v-col>
          <p style="text-align:right">{{ article.created_at }}</p>
        </v-col>
      </v-row>
      <img
        src="https://ichef.bbci.co.uk/news/976/cpsprodpb/CA15/production/_111633715_df2cb9e9-4f34-499d-a255-29abf37d36d0.jpg"
        alt=""
        class="detailimage"
      />
      <div class="showcontent">
        <p>{{ article.content }}</p>
      </div>
      <h2>comment 넣을 곳</h2>
    </div>
  </div>
</template>

<script>
import * as showService from "../../api/show.js";
export default {
  data() {
    return {
      article: {
        title: "",
        content: "",
        username: "",
        created_at: ""
      }
    };
  },
  mounted: function() {
    var showId = this.$route.params.id;
    showService.getShowById(showId, function(response) {
      console.log(response.data);
      const data = response.data;
      this.title = data.title;
      this.content = data.content;
      this.created_at = data.created_at;
      this.username = data.username;
    });

    // show 디테일 조회
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
