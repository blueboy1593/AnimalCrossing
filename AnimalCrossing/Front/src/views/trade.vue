<template>
  <div id="trade">
    <sequential-entrance fromRight>
      <tradeNav />
    </sequential-entrance>
    <router-view />
  </div>
</template>

<script>
import tradeNav from "../components/trade/tradeNav.vue";
export default {
  components: {
    tradeNav
  }
};
</script>

<style scoped>
#trade {
  background-color: none;
}
</style>
