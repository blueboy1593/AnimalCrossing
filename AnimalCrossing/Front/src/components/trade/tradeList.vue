<template>
  <div>
    <div>
      <h2 style="font-family:Gamja Flower">{{ category }}</h2>
      <v-btn>뒤로가기</v-btn>
      <br />
      <tradeItemCard
        v-for="tradeItemCard in tradeItemCards"
        :key="tradeItemCard.id"
        :tradeItemCard="tradeItemCard"
        class="card_one"
      />
    </div>
  </div>
</template>

<script>
import { getTradeById } from "@/api/trade.js";
import tradeItemCard from "./tradeItemCard.vue";

export default {
  name: "trade",
  props: ["category", "id"],
  components: {
    tradeItemCard
  },
  data() {
    return {
      tradeItemCards: []
    };
  },
  async mounted() {
    this.tradeItemCards = await getTradeById(
      this.category,
      this.id,
      this.tradeItemCards
    );
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
