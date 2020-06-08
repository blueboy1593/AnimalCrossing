<template>
  <div>
    <div>
      <button @click="goback" class="backbtn">
        <img
          src="../../assets/images/back.png"
          alt="뒤로가기"
          class="back-img"
        />
      </button>
      <v-tabs color="pink accent-1" background-color="transparent">
        <v-tab @click="buying">
          <img id="buyIcon" src="../../assets/images/buy.png" alt="">
        </v-tab>
        <v-tab @click="selling">
          <img id="sellIcon" src="../../assets/images/sell.png" alt="">
        </v-tab>
      </v-tabs>
      <br />
      <tradeItemCard
        v-for="selectedItemCard in selectedItemCards"
        :key="selectedItemCard.id"
        :tradeItemCard="selectedItemCard"
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
      tradeItemCards: [],
      selectedItemCards: []
    };
  },
  methods: {
    goback() {
      this.$router.go(-1);
    },
    buying() {
      let buyList = this.tradeItemCards.filter(
        tradeItemCard => tradeItemCard.sort === "buy"
      );
      this.selectedItemCards = buyList;
      console.log("삽니다", buyList, this.selectedItemCards);
    },
    selling() {
      let sellList = this.tradeItemCards.filter(
        tradeItemCard => tradeItemCard.sort === "sell"
      );
      this.selectedItemCards = sellList;
      console.log("팝니다", sellList, this.selectedItemCards);
    }
  },
  async mounted() {
    this.tradeItemCards = await getTradeById(
      this.category,
      this.id,
      this.tradeItemCards
    );
    let buyList = this.tradeItemCards.filter(
      tradeItemCard => tradeItemCard.sort === "buy"
    );
    this.selectedItemCards = buyList;
    console.log(this.tradeItemCards);
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

#tabColor::selection {
  background-color: red;
}

#buyingTab {
  background-color: none;
}

#buyIcon {
  width: 55px;
  margin-bottom: 3px;
}

#sellIcon {
  width: 55px;
  margin-bottom: 3px;
}


</style>
