!<template>
  <div>
    <h2 class="btitle">거래해요, 동물의 숲</h2>
    <TradeEtcList />
  </div>
</template>

<script>
import TradeEtcList from "./TradeEtcList.vue";
export default {
  components: { TradeEtcList }
};
</script>

<style scoped>
.btitle {
  font-family: "Jua", sans-serif;
  text-align: center;
  font-size: 1.7rem;
}
</style>
