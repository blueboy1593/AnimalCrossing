<template>
  <div class="community">
    <div class="container">
      <button @click="goback" class="backbtn">
        <img src="../../assets/images/back.png" alt="글쓰기" class="back-img" />
      </button>
      <div class="onetrade">
        <h2 class="ttext" style="margin-bottom: 5px">
          {{ this.article.title }}
        </h2>
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
        <div v-if="article.image === null" class="detailimage">
          <img
            src="https://ichef.bbci.co.uk/news/976/cpsprodpb/CA15/production/_111633715_df2cb9e9-4f34-499d-a255-29abf37d36d0.jpg"
            class="detailimage detailImg"
          />
        </div>
        <div v-else>
          <img
            v-bind:src="article.image"
            alt=""
            class="detailimage detailImg"
          />
        </div>
        <div class="showcontent">
          <p>{{ article.content }}</p>
        </div>
        <!-- <v-btn id="boastDelete" v-if="this.checkId()" color="error" @click="deleteShow">삭제하기</v-btn> -->
        <div id="boastDeleteDiv">
          <button id="boastDelete" v-if="this.checkId()" @click="deleteShow">
            <img
              id="boastDeleteImg"
              src="../../assets/images/삭제.png"
              alt=""
            />
          </button>
        </div>
      </div>
      <h4 class="text">
        <div class="commentImg">
          <input
            id="comment"
            type="text"
            v-model="comment"
            placeholder="댓글을 입력하세요"
            @keyup.enter="writeComment"
          />
          <img
            id="commentImg"
            src="../../assets/images/comment.png"
            alt=""
            v-on:click="writeComment"
          />
        </div>
      </h4>
      <CommentList
        v-on:update="updateComment"
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
import { deleteShows, writeComment } from "../../api/show.js";

export default {
  components: { CommentList },
  data: function() {
    return {
      article: {
        title: "",
        content: "",
        image: null,
        username: "",
        user_id: "",
        created_at: "",
        CommentLists: [], // obj3개 들어감
        show_pk: ""
      },
      comment: ""
    };
  },
  methods: {
    async writeComment() {
      var scope = this;
      const user = this.$store.state.user;
      const show_id = Number(this.$route.params.id);
      const token = this.$store.state.user.token;
      const comment = {
        show: show_id,
        content: this.comment,
        user_id: user.id,
        username: user.username
      };
      console.log(comment);
      await writeComment(comment, show_id, token, async function(response) {
        console.log(response);
        let data = await showService.getShowById(show_id);
        let list = { ...scope.article };
        list.CommentLists = data.showcomments;
        scope.article = list;
        console.log(scope.article);
        scope.comment = "";
      });

      // this.$router.go(this.$router.currentRoute);
      // $router.push("/auction/register/" + response.data.id);
    },
    async updateComment() {
      const show_id = Number(this.$route.params.id);
      let data = await showService.getShowById(show_id);
      let list = { ...this.article };
      console.log("여기에요!!", data, list);
      list.CommentLists = data.showcomments;
      this.article = list;
    },
    checkId() {
      if (this.article.user_id === this.$store.state.user.id) {
        return true;
      }
    },
    async deleteShow() {
      const show_pk = this.$route.params.id;
      const token = this.$store.state.user.token;
      await deleteShows(show_pk, token);
      this.$router.go(-1);
    },
    goback() {
      this.$router.go(-1);
    }
  },
  // detail정보 가져오기
  mounted: async function() {
    var showId = this.$route.params.id;
    const data = await showService.getShowById(showId);
    this.article.CommentLists = data.showcomments;
    this.article.title = data.title;
    this.article.image = data.image;
    this.article.content = data.content;
    this.article.created_at =
      data.created_at.substring(0, 10) +
      "  " +
      data.created_at.substring(11, 16);
    this.article.username = data.username;
    this.article.user_id = data.user_id;
  }
};
</script>

<style scoped>
.detailimage {
  width: 400px;
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
  margin-top: 10px;
  text-align: center;
  font-family: "Gamja Flower", cursive;
}
.showcontent {
  font-size: 1.2rem;
  text-align: center;
  margin-top: 10px;
  margin-bottom: 10px;
  font-family: "Gamja Flower", cursive;
}
.text {
  font-family: "Gamja Flower", cursive;
  margin-left: 1rem;
}

#comment {
  display: inline-block;
  background-color: rgba(210, 241, 31, 0.37);
  width: 80%;
  height: 50px;
  border-radius: 13px;
  font-family: "Jua", sans-serif;
  text-align: center;
}

#comment:focus {
  outline: none;
}

/* 한줄로 해주기 위해 flex!! */
.commentImg {
  display: flex;
  align-items: center;
  justify-content: center;
}

#commentImg {
  margin: 10px 10px 10px 15px;
  width: 70px;
}

#commentImg:hover {
  transform: scale(1.1);
  animation: commentButton-ani 1s forwards;
}

@keyframes commentButton-ani {
  0% {
    opacity: 0.8;
    transform: scale(0.95);
  }

  50% {
    opacity: 1;
    transform: scale(1.3);
  }

  100% {
    opacity: 1;
    transform: scale(1.1);
  }
}
.onetrade {
  background-color: rgba(30, 255, 135, 0.075);
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
  border-bottom: 1.2px solid rgba(76, 180, 157, 0.295);
  margin-bottom: 0.3rem;
  display: grid;
}

#boastDeleteDiv {
  display: flex;
  justify-content: center;
  /* 오른쪽 정렬 */
  /* justify-content: flex-end; */
}

#boastDelete {
  max-width: 64px;
  border: 0;
  outline: 0;
}

#boastDeleteImg {
  width: 100%;
}

#boastDeleteImg:hover {
  transform: scale(1.1);
}
.back-img {
  height: 25px;
  margin-right: 30px;
}
.backbtn {
  border: 0;
  outline: 0;
}
</style>
