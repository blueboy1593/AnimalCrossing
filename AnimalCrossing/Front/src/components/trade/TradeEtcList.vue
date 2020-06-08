<template>
  <div>
    <div>
      <button @click="goback" class="backbtn">
        <!-- <img
          src="../../assets/images/back.png"
          alt="뒤로가기"
          class="back-img"
        /> -->
        <img src="../../assets/images/back1.png" alt="뒤로가기" />
        <img src="../../assets/images/back2.png" alt="뒤로가기" />
      </button>
      <!-- <v-tabs>
        <v-tab @click="buying">삽니다</v-tab>
        <v-tab @click="selling">팝니다</v-tab>
      </v-tabs> -->
      <v-tabs centered color="pink accent-1" background-color="transparent">
        <v-tab @click="selling">
          <img id="sellIcon" src="../../assets/images/sell.png" alt="" />
        </v-tab>
        <v-tab @click="buying">
          <img id="buyIcon" src="../../assets/images/buy.png" alt="" />
        </v-tab>
      </v-tabs>
      <br />
      <div style="display: flex;">
        <v-text-field
          v-model="searchText"
          @keyup="filter"
          solo-inverted
          flat
          hide-details
          label="Search"
          class="nav-search"
        ></v-text-field>
      </div>
      <TradeEtcCard
        v-for="selectedItemCard in searchItemCards"
        :key="selectedItemCard.id"
        :TradeEtcCard="selectedItemCard"
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
      TradeEtcCards: [],
      selectedItemCards: [],
      searchItemCards: [],
      searchText: ""
    };
  },
  methods: {
    filter() {
      let check = this.selectedItemCards.filter(
        selectedItemCard =>
          selectedItemCard.title.indexOf(this.searchText.trim()) !== -1 ||
          selectedItemCard.content.indexOf(this.searchText.trim()) !== -1
      );
      this.searchItemCards = check;
      console.log(check);
    },
    goback() {
      this.$router.go(-1);
    },
    buying() {
      let buyList = this.TradeEtcCards.filter(
        TradeEtcCard => TradeEtcCard.sort === "buy"
      );
      this.selectedItemCards = buyList;
      console.log("삽니다", buyList, this.selectedItemCards);
    },
    selling() {
      let sellList = this.TradeEtcCards.filter(
        TradeEtcCard => TradeEtcCard.sort === "sell"
      );
      this.selectedItemCards = sellList;
      console.log("팝니다", sellList, this.selectedItemCards);
    }
  },
  async mounted() {
    this.TradeEtcCards = await getTradeListEtc(this.TradeEtcCards);
    let sellList = this.TradeEtcCards.filter(
      TradeEtcCard => TradeEtcCard.sort === "sell"
    );
    this.selectedItemCards = sellList;
    console.log(this.selectedItemCards);
    this.searchItemCards = sellList;
  }
};
</script>

<style scoped>
.v-text-field {
  width: 300px;
  background-color: rgba(173, 204, 245, 0.322);
  margin-bottom: 10px;
  margin-left: 35%;
  margin-right: 35%;
}
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
  display: block;
  border: 0;
  outline: 0;
}

.backbtn img:last-child {
  display: none;
}
.backbtn:hover img:first-child {
  display: none;
}
.backbtn:hover img:last-child {
  display: inline-block;
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
