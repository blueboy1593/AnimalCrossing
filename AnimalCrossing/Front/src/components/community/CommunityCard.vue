<template>
  <div>
    <router-link :to="{ name: 'cdetail', params: { id: communityCard.id } }">
      <div @click="toDetail" class="cCard">
        <div class="cphoto">
          <div v-if="communityCard.image === null">
            <img
              src="https://ichef.bbci.co.uk/news/976/cpsprodpb/CA15/production/_111633715_df2cb9e9-4f34-499d-a255-29abf37d36d0.jpg"
              class="cimage"
            />
          </div>
          <div v-else>
            <img v-bind:src="communityCard.image" alt="" class="detailimage" />
          </div>
        </div>
        <div class="infoName">
          {{ communityCard.title }}
        </div>
        <v-row>
          <div class="infoDetail3">
            {{ communityCard.username }}
          </div>
          <div class="infoDetail2">
            {{ this.counter }}
          </div></v-row
        >
      </div>
    </router-link>
  </div>
</template>

<script>
export default {
  name: "communityCard",
  props: ["communityCard"],
  data: function() {
    return {
      counter: this.communityCard.created_at,
      id: this.communityCard.id
    };
  },
  computed: {
    trim: function() {
      return this.counter.substring(0, 5);
    }
  },
  methods: {
    toDetail: function() {
      console.log(this.id);
      this.$router.push({ path: `/community/detail/${this.id}` });
    }
  }
};
</script>

<style>
.cCard {
  margin-top: 0.3rem;
  width: 100%;
  height: 20%;
  border-radius: 15px;
  border-style: dotted;
  border-color: #76a7b2;
  border-width: 5px;
  overflow: hidden;
}

.cphoto {
  width: 100%;
  height: 20%;
  border-radius: 15px;
  text-align: center;
  overflow: hidden;
}

.cimage {
  height: 170px;
  display: block;
  margin: 0 auto;
}

.infoName {
  text-align: center;
  font-weight: bolder;
  font-size: 1rem;
  font-family: "Gamja Flower", cursive;
}

.infoDetail3 {
  font-weight: 100;
  font-family: "Gamja Flower", cursive;
  /* margin-left: 15px; */
}
.infoDetail2 {
  text-align: right;
  font-weight: 100;
  font-family: "Gamja Flower", cursive;
}
</style>
