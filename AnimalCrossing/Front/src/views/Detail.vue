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
export default {
  data() {
    return {
      article: {
        title: "제목입니다만",
        content:
          "내용 블라블라 🏝️모여봐요 동물의 숲🏝️ 🌞하루 24시간 BGM🌛 🏖️동물의 숲 하루를 채우는 잔잔한 노래🌊🏝️모여봐요 동물의 숲🏝 🌞하루 24시간 BGM🌛 🏖️동물의 숲 하루를 채우는 잔잔한 노래🌊",
        username: "paik11012",
        created_at: "2020-06-03"
      }
    };
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
