<template>
  <div class="community">
    <div class="container">
      <h2 class="ttext" style="margin-bottom: 5px">{{ this.article.title }}</h2>
      <v-row no-gutters>
        <v-col>
          <p class="text">{{ this.article.username }}</p>
        </v-col>
        <v-col>
          <p style="text-align:right" class="text">
            {{ this.article.created_at }}
          </p>
        </v-col>
      </v-row>
      <div v-if="this.image == null" class="detailimage">
        <img
          src="https://ichef.bbci.co.uk/news/976/cpsprodpb/CA15/production/_111633715_df2cb9e9-4f34-499d-a255-29abf37d36d0.jpg"
          class="detailimage detailImg"
        />
      </div>
      <div v-else>
        <img v-bind:src="article.image" alt="" class="detailimage detailImg" />
      </div>
      <div class="showcontent">
        <p>{{ article.content }}</p>
      </div>
      <v-btn color="error">삭제하기</v-btn>
      <h4 class="text">
        <div class="commentImg">
          <img id="commentImg" src="../../assets/images/comment.png" alt="">
        </div>
      </h4>
      <CommentList
        v-for="CommentList in article.CommentLists"
        :key="CommentList.id"
        :CommentList="CommentList"
      />
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
        image: null,
        username: "",
        created_at: "",
        CommentLists: [] // obj3개 들어감
      }
    };
  },
  mounted: async function() {
    var showId = this.$route.params.id;
    const data = await showService.getShowById(showId);
    this.article.CommentLists = data.showcomments;
    console.log(this.article.CommentLists); // object
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
  width: 70%;
  align-items: center;
  display: block;
  margin: 0px auto;
  border-radius: 10px;
}

.detailImg {
  box-shadow: 4px 4px 3px 0px rgba(4, 37, 56, 0.75);
}

.detailImg:hover {
  transform: scale(1.02);
  opacity: 0.95;
}

.ttext {
  text-align: center;
  font-family: "Gamja Flower", cursive;
}
.showcontent {
  margin-top: 10px;
  font-family: "Gamja Flower", cursive;
}
.text {
  font-family: "Gamja Flower", cursive;
}

#commentImg {
  margin: 10px 10px;
  width: 70px;
}
</style>
