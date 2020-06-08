<template>
  <div>
    <div>
      <button @click="goback" class="backbtn">
        <img src="../../assets/images/back.png" alt="글쓰기" class="back-img" />
      </button>
      <br />
      <tradeItemCard
        v-for="tradeItemCard in tradeItemCards"
        :key="tradeItemCard.id"
        :tradeItemCard="tradeItemCard"
        :name="tradeItemCard.engname"
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
  props: ["category", "id", "name"],
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
  },
  methods: {
    goback() {
      this.$router.go(-1);
    }
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
.back-img {
  height: 25px;
  margin-right: 30px;
}
.backbtn {
  border: 0;
  outline: 0;
}
</style>
