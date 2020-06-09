<template>
  <div>
    <router-link :to="{ name: 'cdetail', params: { id: MypageCard.id } }">
      <div class="cCard">
        <div class="cphoto">
          <div v-if="MypageCard.image === null">
            <img
              src="https://ichef.bbci.co.uk/news/976/cpsprodpb/CA15/production/_111633715_df2cb9e9-4f34-499d-a255-29abf37d36d0.jpg"
              class="cimage"
            />
          </div>
          <div v-else>
            <img v-bind:src="MypageCard.image" alt="" class="detailimage" />
          </div>
        </div>
        <div class="infoName">
          {{ MypageCard.title }}
        </div>
      </div>
    </router-link>
  </div>
</template>

<script>
export default {
  props: ["MypageCard"]
};
</script>

<style scoped>
.cCard {
  display: inline-block;
  width: 80%;
  height: auto;
  max-height: 165px;
  border-radius: 15px;
  /* margin-right: 1rem; */
  overflow: hidden;
  /* margin-left: 0.5rem; */
  color: black;
  background-color: rgba(110, 173, 157, 0.144);
}

.cCard:hover {
  /* border-bottom: 1px solid #76a7b2; */
  background-color: rgba(98, 173, 155, 0.26);
  transform: scale(1.03);
  opacity: 0.9;
  box-shadow: 0 0 0 1px #76a7b2;
}

.cphoto {
  display: flex;
  /* align-items: center; */
  justify-content: center;
  width: auto;
  height: auto;
  /* min-height: 246.4px; */
  max-width: 230px;
  max-height: 120px;
  /* height: 20%; */
  border-radius: 15px;
  text-align: center;
  overflow: hidden;
}

.cimage {
  max-height: 170px;
  display: block;
  margin: 0 auto;
  margin-top: 4%;
}

.detailimage {
  width: auto;
  /* width: 100%; */
  height: auto;
  max-width: 230px;
  max-height: 120px;
  /* margin-top: 4%; */
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
  margin-left: 10px;
}

.infoDetail2 {
  text-align: right;
  font-weight: 100;
  font-family: "Gamja Flower", cursive;
  margin-right: 10px;
}
</style>
