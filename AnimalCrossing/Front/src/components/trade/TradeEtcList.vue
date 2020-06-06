<template>
  <div>
    <div>
      <br />
      <TradeEtcCard
        v-for="TradeEtcCard in TradeEtcCards"
        :key="TradeEtcCard.id"
        :TradeEtcCard="TradeEtcCard"
        class="card_one"
      />
    </div>
  </div>
</template>

<script>
import { getTradeListEtc } from "@/api/trade.js";
import TradeEtcCard from "./TradeEtcCard.vue";

export default {
  name: "tradeEtc",
  components: {
    TradeEtcCard
  },
  data() {
    return {
      TradeEtcCards: []
    };
  },
  async mounted() {
    this.TradeEtcCards = await getTradeListEtc(this.TradeEtcCards);
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
