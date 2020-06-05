<template>
  <div>
      <div  class="cCard">
        <div class="cphoto">
        </div>
        <div class="infoName">
          {{ tradeCard.price }}
        </div>
          <div class="infoDetail3">
            {{ tradeCard.content }}
          </div>
      </div>
  </div>
</template>

<script>
export default {
  name: "tradeItemCard",
  props: ["tradeCard"],
};
</script>

<style scoped>
.cCard {
  display: inline-block;
  margin-top: 0.3rem;
  width: 26rem;
  height: 20%;
  border-radius: 15px;
  margin-right: 1rem;
  overflow: hidden;

  background-color: rgba(110, 173, 157, 0.144);
}

.cCard:hover {
  border-bottom: 1px solid #76a7b2;
  background-color: rgba(98, 173, 155, 0.26);
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

.detailimage {
  width: 100%;
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
  margin-left: 20px;
}

.infoDetail2 {
  text-align: right;
  font-weight: 100;
  font-family: "Gamja Flower", cursive;
}
</style>
