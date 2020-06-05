<template>
  <div>
    <div>
      <h2 style="font-family:Gamja Flower">거래해요, 동물의 숲</h2>
      <tradeCard
        v-for="tradeCard in tradeCards"
        :key="tradeCard.id"
        :tradeCard="tradeCard"
        class="card_one"
      />
    </div>
  </div>
</template>

<script>
// import { getTradeById } from "@/api/trade.js";
import tradeCard from "./tradeItemCard.vue";

export default {
  name: "trade",
  components: {
    tradeCard
  },
  data() {
    return {
      tradeCards: [],
    };
  },
  async mounted() {
    console.log(this.category, this.infoCard)
    // this.inftradeCards = await getTradeById(this.category, this.tradeCard.id);
  }
};
</script>

<style scoped>
.card_one {
  display: inline-block;
}

.write_btn {
  border: 0;
  background: none;
  display: inline-block;
  margin: 10px auto 0px;
  text-align: center;
  padding: 0px 40px;
  height: 40px;
  outline: none;
  color: black;
  border-radius: 24px;
  transition: 0.25s;
  cursor: pointer;
  border: 2px solid #e46fc7;
}

.write_btn:hover {
  background: #e46fc7;
}
</style>
