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
      <v-tabs centered color="pink accent-1" background-color="transparent">
        <v-tab @click="selling">
          <img id="sellIcon" src="../../assets/images/sell.png" alt="" />
        </v-tab>
        <v-tab @click="buying">
          <img id="buyIcon" src="../../assets/images/buy.png" alt="" />
        </v-tab>
      </v-tabs>
      <br />
      <tradeItemCard
        v-for="selectedItemCard in selectedItemCards"
        :key="selectedItemCard.id"
        :tradeItemCard="selectedItemCard"
        :category="category"
        :engname="engname"
        class="card_one"
      />
    </div>
  </div>
</template>

<script>
import { getTradeById } from "@/api/trade.js";
import tradeItemCard from "./tradeItemCard.vue";
import * as infoService from "../../api/info.js";
export default {
  name: "trade",
  props: ["category", "id"],
  components: {
    tradeItemCard
  },
  data() {
    return {
      tradeItemCards: [],
      selectedItemCards: [],
      engname: ""
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
    },
    selling() {
      let sellList = this.tradeItemCards.filter(
        tradeItemCard => tradeItemCard.sort === "sell"
      );
      this.selectedItemCards = sellList;
    }
  },
  async mounted() {
    this.tradeItemCards = await getTradeById(
      this.category,
      this.id,
      this.tradeItemCards
    );
    let sellList = this.tradeItemCards.filter(
      tradeItemCard => tradeItemCard.sort === "sell"
    );
    this.selectedItemCards = sellList;
    let data = "";
    if (this.category === "fossil") {
      return;
    }
    if (this.category === "animal") {
      data = await infoService.getNeighbors();
    } else if (this.category === "painting") {
      data = await infoService.getPaintings();
    }
    let find = data.filter(element => this.id == element.id);

    this.engname = find[0].engname;
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
